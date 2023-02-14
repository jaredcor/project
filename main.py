import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from cryptography.fernet import Fernet
import csv
from numpy.random import seed
from numpy.random import randint


class Patient:
    def __init__(self, name, bill):
        self.name = name
        self.bill = bill

    def __str__(self):
        return f"{self.name}"


# setup gui
master = Tk()
master.title("Secure Health Information System")
master.geometry("300x300")

# setup files
questions_file = open("data/questions.csv", "a", encoding="UTF8")
results_file = open("data/results.csv", "r")
refill_file = open("data/refill.csv", "r")
payment_file = open("data/payment.csv", "r")

# setup encryption & decryption
key = Fernet.generate_key()
fernet = Fernet(key)

# vars
patient1 = Patient("Jared Cortez", 0)
recipient_var = tk.StringVar()
question_var = tk.StringVar()
marijuana_price = 300
lexapro_price = 500
payment_information_var = tk.StringVar()

# utility functions


def submit():
    recipient = recipient_var.get()
    question = question_var.get()

    # test
    print("Recipient: " + recipient)
    print("Question: " + question)
    # encrypt question to store
    enc_question = fernet.encrypt(question.encode())
    print("Encrypted Question: " + str(enc_question))

    # write to csv
    writer = csv.writer(questions_file)
    data = [recipient, enc_question]
    writer.writerow(data)

    recipient_var.set("")
    question_var.set("")


def open_show_results_window1():
    show_results_window = Toplevel(master)
    show_results_window.geometry("300x300")

    reader = csv.reader(results_file)
    reader = list(reader)
    result = reader[1][1]
    date = reader[1][0]
    print("{}:{}".format(date, result))

    # print("encrypted result: ", result)
    # dec_result = fernet.decrypt(result).decode()
    # print("decrypted result: ", dec_result)

    Label(show_results_window, text="Your results from {}:".format(date)).pack(pady=10)
    Message(show_results_window, text=result).pack(pady=10)

    close_button = Button(show_results_window, text="Close",
                          command=show_results_window.destroy)
    close_button.pack(pady=20)


def open_show_results_window2():
    show_results_window = Toplevel(master)
    show_results_window.geometry("300x300")

    reader = csv.reader(results_file)
    reader = list(reader)
    result = reader[2][1]
    date = reader[2][0]
    print("{}:{}".format(date, result))

    Label(show_results_window, text="Your results from {}:".format(date)).pack(pady=10)
    Message(show_results_window, text=result).pack(pady=10)

    close_button = Button(show_results_window, text="Close",
                          command=show_results_window.destroy)
    close_button.pack(pady=20)


def open_show_results_window3():
    show_results_window = Toplevel(master)
    show_results_window.geometry("300x300")

    reader = csv.reader(results_file)
    reader = list(reader)
    result = reader[3][1]
    date = reader[3][0]
    print("{}:{}".format(date, result))

    Label(show_results_window, text="Your results from {}:".format(date)).pack(pady=10)
    Message(show_results_window, text=result).pack(pady=10)

    close_button = Button(show_results_window, text="Close",
                          command=show_results_window.destroy)
    close_button.pack(pady=20)


def open_transaction_window():
    transaction_window = Toplevel(master)
    transaction_window.geometry("640x640")

    Label(transaction_window, text="Enter credit card information:").pack(pady=10)
    payment_information_entry = Entry(
        transaction_window, textvariable=payment_information_var)
    payment_information_entry.pack(pady=10)

    seed(1)
    confirmation_number = randint(0, 10, 10)
    confirmation_number = confirmation_number.astype(str)
    tmp = ""
    confirmation_number = tmp.join(confirmation_number)
    success_msg = Message(transaction_window, text="Payment successful!")
    confirmation_msg = Message(
        transaction_window, text="Confirmation number: {}".format(confirmation_number))

    def transaction():
        patient_payment_information = payment_information_var.get()
        csvr = csv.reader(payment_file)
        csvr = list(csvr)

        patient_card_number = csvr[1][0]
        print("Card:", patient_card_number)
        patient_checking_account = csvr[1][1]
        patient_checking_account = int(patient_checking_account)
        print("Patient checking account: $", patient_checking_account)
        if patient_payment_information == patient_card_number:
            print("Bill: $", patient1.bill)
            if patient_checking_account >= patient1.bill:
                print("Payment successful.")
                success_msg.pack(pady=10)
                confirmation_msg.pack(pady=10)
                patient_checking_account -= patient1.bill
            elif patient_checking_account < patient1.bill:
                print("Card declined.")
                transaction_window.destroy()

    submit_button = Button(
        transaction_window, text="Submit", command=transaction)
    submit_button.pack(pady=10)

    cancel_button = Button(transaction_window, text="Cancel",
                           command=transaction_window.destroy)
    cancel_button.pack(pady=10)


# use cases
def open_ask_questions_window():
    ask_questions_window = Toplevel(master)
    ask_questions_window.title("Ask Questions")
    ask_questions_window.geometry("640x640")

    # text
    Label(ask_questions_window, text="Our Staff").pack(pady=10)
    msg = "Olivia Robinson, MD\nAngus Small, MD\nHanna Chandler, BSN\nMalakai Duffy, BSN\nElijah Branch, BSN\nOtto Lawson, BSN"
    Message(ask_questions_window, text=msg).pack(pady=10)

    # text boxes
    recipient_label = Label(ask_questions_window, text="To:")
    recipient_label.pack(pady=10)
    recipient_entry = Entry(ask_questions_window, textvariable=recipient_var)
    recipient_entry.pack(pady=10)
    question_label = Label(ask_questions_window, text="Enter question:")
    question_label.pack(pady=10)
    question_entry = Entry(ask_questions_window, textvariable=question_var)
    question_entry.pack(pady=10)

    # submit
    submit_button = Button(ask_questions_window, text="Submit", command=submit)
    submit_button.pack(pady=10)


def open_see_test_results_window():
    see_test_results_window = Toplevel(master)
    see_test_results_window.title("See Test Results")
    see_test_results_window.geometry("640x640")

    # text
    Label(see_test_results_window, text="Your results").pack(pady=10)

    # buttons
    # result1_button = Button(see_test_results_window,
    #                         text="11/25/22", command=open_show_results_window1())
    # result1_button.pack(pady=10)

    # result2_button = Button(see_test_results_window,
    #                         text="11/27/22", command=open_show_results_window2())
    # result2_button.pack(pady=10)

    # result3_button = Button(see_test_results_window,
    #                         text="12/2/22", command=open_show_results_window3())
    # result3_button.pack(pady=10)
    lb = Listbox(see_test_results_window, selectmode=SINGLE)
    lb.insert(1, "11/25/22")
    lb.insert(2, "11/27/22")
    lb.insert(3, "12/2/22")
    lb.pack(pady=10)

    def selected_item():
        for i in lb.curselection():
            if lb.get(i) == "11/25/22":
                open_show_results_window1()
            elif lb.get(i) == "11/27/22":
                open_show_results_window2()
            elif lb.get(i) == "12/2/22":
                open_show_results_window3()

    submit_button = Button(
        see_test_results_window, text="Submit", command=selected_item)
    submit_button.pack(pady=10)

    cancel_button = Button(see_test_results_window, text="Cancel",
                           command=see_test_results_window.destroy)
    cancel_button.pack(pady=10)


def open_request_refill_window():
    request_refill_window = Toplevel(master)
    request_refill_window.title("Request Refills")
    request_refill_window.geometry("640x640")

    # file decryption
    csvr = csv.reader(refill_file)
    csvr = list(csvr)
    # dec_medication = []
    # dec_information = []
    # # for i in csvr:
    # #     dec_medication.append(fernet.decrypt(csvr[i][0]).decode())
    # #     dec_information.append(fernet.decrypt(csvr[0][i]).decode())
    # tmp = str(csvr[1][0])
    # print(tmp)
    # tmp2 = fernet.decrypt(tmp).decode
    # dec_medication.append(tmp2)
    # print(dec_medication)

    # for i in refill_csv:
    #     print(dict(i))

    # text
    Label(request_refill_window, text="Your medications:").pack(pady=10)
    lb = Listbox(request_refill_window, selectmode=SINGLE)
    # for i in csvr:
    #     lb.insert(i, csvr[i][0])
    lb.insert(1, csvr[1][0])
    lb.insert(2, csvr[2][0])
    lb.pack(pady=10)

    Label(request_refill_window, text="Information:").pack(pady=10)
    txt1 = "{}: {}".format(csvr[1][0], csvr[1][1])
    txt2 = "{}: {}".format(csvr[2][0], csvr[2][1])
    Message(request_refill_window,
            text="{}\n\n{}".format(txt1, txt2)).pack(pady=10)

    def selected_item():
        for i in lb.curselection():
            print(lb.get(i))
            Message(request_refill_window, text="{} refill submitted.".format(
                lb.get(i))).pack(pady=10)
            if lb.get(i) == "Lexapro":
                patient1.bill += lexapro_price
                print(patient1.bill)
            elif lb.get(i) == "Medical Marijuana":
                patient1.bill += marijuana_price
                print(patient1.bill)

    refill_info_button = Button(
        request_refill_window, text="Submit", command=selected_item)
    refill_info_button.pack(pady=10)

    def cancel_request_refill():
        patient1.bill = 0
        request_refill_window.destroy()

    cancel_button = Button(request_refill_window, text="Cancel",
                           command=cancel_request_refill)
    cancel_button.pack(pady=10)


def open_pay_bill_window():
    pay_bill_window = Toplevel(master)
    pay_bill_window.title("Pay Bill")
    pay_bill_window.geometry("640x640")

    Label(pay_bill_window, text="Bill total: ${}".format(
        patient1.bill)).pack(pady=10)

    pay_now_button = Button(pay_bill_window, text="Pay Now",
                            command=open_transaction_window)
    pay_now_button.pack(pady=10)

    cancel_button = Button(pay_bill_window, text="Cancel",
                           command=pay_bill_window.destroy)
    cancel_button.pack(pady=10)


label = Label(master, text="Welcome back, " + patient1.name + "!")

label.pack(pady=10)

ask_button = Button(master, text="Ask Questions",
                    command=open_ask_questions_window)
ask_button.pack(pady=10)

test_results_button = Button(master, text="See Test Results",
                             command=open_see_test_results_window)
test_results_button.pack(pady=10)

refill_button = Button(master, text="Request Refills",
                       command=open_request_refill_window)
refill_button.pack(pady=10)

pay_button = Button(master, text="Pay Bill",
                    command=open_pay_bill_window)
pay_button.pack(pady=10)


mainloop()

# close files
questions_file.close()
results_file.close()
refill_file.close()
payment_file.close()
