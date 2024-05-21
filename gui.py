import tkinter as tk
import tkinter.font as tkFont
from multithreading import main_loop
from tkinter import PhotoImage
from tkinter import messagebox
from datetime import datetime, timedelta


def start_monitoring(start_date, end_date, start_time, end_time, interval_minutes, second_interval_minutes,
                     target_addresses, selected_functions):
    messagebox.showinfo("Start Monitoring", "Monitoring started!")

    print("Start Date:", start_date)
    print("End Date:", end_date)
    print("Start Time:", start_time)
    print("End Time:", end_time)
    print("Interval Minutes:", interval_minutes)
    print("Second Interval Minutes:", second_interval_minutes)
    print("Target Addresses:", target_addresses)
    print("Selected Functions:", selected_functions)
    target_addresses = target_addresses

    main_loop(start_date, end_date, start_time, end_time, interval_minutes, second_interval_minutes,
              target_addresses, selected_functions)


def stop_monitoring():
    messagebox.showinfo("Stop Monitoring", "Monitoring stopped!")


def show_error(message):
    messagebox.showerror("Error", message)


def validate_and_start(start_date_entry, end_date_entry, start_time_entry, end_time_entry, interval_minutes_entry,
                       second_interval_minutes_entry, target_addresses_entry, functions):
    # خواندن و اعتبارسنجی ورودی‌ها از فرم
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    start_time = start_time_entry.get()
    end_time = end_time_entry.get()
    interval_minutes = interval_minutes_entry.get()
    second_interval_minutes = second_interval_minutes_entry.get()
    target_addresses = target_addresses_entry.get()

    selected_functions = []
    for var, option_text in zip(functions, ["Get Ping", "Get Status", "Get Load Time", "All"]):
        if var.get():  # اگر مقدار متغیر متصل به گزینه True باشد
            selected_functions.append(option_text)

    if "All" in selected_functions:
        selected_functions = ["All"]

    # اعتبارسنجی تاریخ‌ها و زمان‌ها
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        start_time = datetime.strptime(start_time, "%H:%M:%S").time()
        end_time = datetime.strptime(end_time, "%H:%M:%S").time()
    except ValueError:
        show_error("Invalid date or time format.")
        return

    # اعتبارسنجی سایر ورودی‌ها (می‌توانید اعتبارسنجی دقیق‌تری انجام دهید)
    if not interval_minutes.isdigit() or not second_interval_minutes.isdigit():
        show_error("Interval values must be integers.")
        return

    if not selected_functions:
        show_error("Choose at least one option.")
        return

    # شروع مانیتورینگ با ورودی‌های اعتبارسنجی شده
    start_monitoring(str(start_date), str(end_date), str(start_time), str(end_time), int(interval_minutes),
                     int(second_interval_minutes), target_addresses, selected_functions)
    messagebox.showinfo('Finish', "The program ended successfully.")
    return


def update_clock(label):
    current_time = datetime.now().strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, lambda: update_clock(label))


# تابع برای متوقف کردن برنامه
def stop_program(root):
    root.destroy()


def adjust_date(entry, delta_days):
    current_date = datetime.strptime(entry.get(), "%Y-%m-%d").date()
    new_date = current_date + timedelta(days=delta_days)
    entry.delete(0, tk.END)
    entry.insert(0, new_date.strftime("%Y-%m-%d"))


def create_new_window():
    new_window = tk.Toplevel(root)
    new_window.title(f"Monitoring Configuration")
    create_monitoring_form(new_window)


def create_monitoring_form(window):
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    tk.Label(window, text="Start Date").grid(row=0, column=0)
    start_date_entry = tk.Entry(window)
    start_date_entry.insert(0, current_date)
    start_date_entry.grid(row=0, column=1)

    tk.Label(window, text="End Date").grid(row=1, column=0)
    end_date_entry = tk.Entry(window)
    end_date_entry.insert(0, current_date)
    end_date_entry.grid(row=1, column=1)

    tk.Label(window, text="Start Time").grid(row=2, column=0)
    start_time_entry = tk.Entry(window)
    start_time_entry.insert(0, current_time)
    start_time_entry.grid(row=2, column=1)

    tk.Label(window, text="End Time").grid(row=3, column=0)
    end_time = datetime.now() + timedelta(hours=5)
    end_time_str = end_time.strftime("%H:%M:%S")
    end_time_entry = tk.Entry(window)
    end_time_entry.insert(0, end_time_str)
    end_time_entry.grid(row=3, column=1)

    tk.Label(window, text="Interval Minutes").grid(row=4, column=0)
    interval_minutes_entry = tk.Entry(window)
    interval_minutes_entry.insert(0, '2')
    interval_minutes_entry.grid(row=4, column=1)

    tk.Label(window, text="Second Interval Minutes").grid(row=5, column=0)
    second_interval_minutes_entry = tk.Entry(window)
    second_interval_minutes_entry.insert(0, '5')
    second_interval_minutes_entry.grid(row=5, column=1)

    tk.Label(window, text="Target Addresses").grid(row=6, column=0)
    target_addresses_entry = tk.Entry(window)
    target_addresses_entry.insert(0, 'hammura.com')
    target_addresses_entry.grid(row=6, column=1)

    options_frame = tk.Frame(window)
    options_frame.grid(row=7, column=0, columnspan=4, pady=10, sticky="W")

    tk.Label(options_frame, text="Options:").grid(row=0, column=0)
    options_vars = []
    options_texts = ["Get Ping", "Get Status", "Get Load Time", "All"]
    for i, option_text in enumerate(options_texts):
        var = tk.BooleanVar()
        checkbutton = tk.Checkbutton(options_frame, text=option_text, variable=var)
        checkbutton.grid(row=0, column=1 + i, sticky="W")
        options_vars.append(var)

    clock_label = tk.Label(window, text="", font=('Helvetica', 12))
    clock_label.grid(row=20, column=0, columnspan=5)
    update_clock(clock_label)

    button_frame = tk.Frame(window)
    button_frame.grid(row=8, column=0, columnspan=1, pady=10)

    play_button = tk.Button(button_frame, image=play_image, font=font_awesome,
                            command=lambda: validate_and_start(start_date_entry, end_date_entry, start_time_entry,
                                                               end_time_entry, interval_minutes_entry,
                                                               second_interval_minutes_entry,
                                                               target_addresses_entry,
                                                               options_vars), bg='green')
    play_button.pack(side=tk.LEFT, padx=5)

    stop_button = tk.Button(button_frame, image=stop_image, font=font_awesome, command=lambda: stop_program(window),
                            bg='red')
    stop_button.pack(side=tk.LEFT, padx=5)

    new_address_button = tk.Button(button_frame, image=add_image, font=font_awesome, bg='blue',
                                   command=create_new_window)
    new_address_button.pack(side=tk.RIGHT, padx=5)


def create_monitoring_configuration_window():
    global root, play_image, stop_image, add_image, font_awesome

    root = tk.Tk()
    root.title("Monitoring Configuration")

    play_image = PhotoImage(file="./play.png")
    stop_image = PhotoImage(file="./stop.png")
    add_image = PhotoImage(file="./plus.png")
    font_awesome = tkFont.Font(family="FontAwesome", size=12)

    create_monitoring_form(root)

    root.mainloop()


create_monitoring_configuration_window()
