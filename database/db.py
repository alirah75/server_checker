from datetime import datetime

from sqlalchemy import create_engine, Column, Date, Integer, String, TIME, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///server_checker.db', echo=False)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Information(Base):
    __tablename__ = 'information'
    id = Column(Integer, primary_key=True, autoincrement=True)
    start_date = Column(String, nullable=False)
    end_date = Column(String, nullable=False)
    start_time = Column(String, nullable=False)
    end_time = Column(String, nullable=False)
    interval_minutes = Column(String, nullable=False)
    second_interval_minutes = Column(String, nullable=False)
    target_addresses = Column(String, nullable=False)
    selected_functions = Column(String, nullable=False)
    status = Column(Integer, nullable=False)


class Log(Base):
    __tablename__ = "log"
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('information.id'))
    server_address = Column(String)
    message = Column(String)
    date = Column(Date, default=datetime.today())
    time = Column(TIME, default=datetime.now())
    information = relationship(Information)


def add_log(project_id, server_address, message):
    session = Session()
    log = Log(project_id=project_id, server_address=server_address, message=message)
    session.add(log)
    session.commit()


def add_information(start_date: str, end_date: str, start_time: str, end_time: str, interval_minutes: int,
                    second_interval_minutes: int, target_addresses: str = None, selected_functions: str = None,
                    status: int = 0):
    session = Session()
    info = Information(start_date=start_date, end_date=end_date, start_time=start_time, end_time=end_time,
                       interval_minutes=interval_minutes, second_interval_minutes=second_interval_minutes,
                       target_addresses=target_addresses, selected_functions=selected_functions, status=status)
    session.add(info)
    session.commit()

# Base.metadata.create_all(engine)
