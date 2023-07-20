from tkinter import *
import random
import time


class GUI:
    def __init__(self):
        self.__main_window = Tk()
        self.__main_window.title("Wordle!")
        self.__main_window.geometry("800x600")

        # Creating the components of the GUI
        self.__game_label = Label(self.__main_window,
                                  text="WORDLE", font=('Helvetica', 80))
        self.__game_label.pack()
        self.main_menu()
        self.__end_time = None  # Initialize end time
        self.__user_name = None  # Initialize user name
        self.__main_window.mainloop()

    def main_menu(self):
        self.__new_game_frame = Frame(self.__main_window)
        self.__new_game_button = Button(self.__new_game_frame, text="New Game",
                                        height=3, width=10,
                                        command=self.enter_user_name)
        self.__new_game_button.pack()
        self.__instructions_button = Button(self.__new_game_frame,
                                            text="Instructions", height=3,
                                            width=10,
                                            command=self.instructions_window)
        self.__instructions_button.pack()
        self.__leaderboard_button = Button(self.__new_game_frame,
                                           text="Leaderboard", height=3,
                                           width=10,
                                           command=self.leaderboard_window_display)
        self.__leaderboard_button.pack()
        self.__quit_button = Button(self.__new_game_frame, text="Quit",
                                    height=3, width=10, command=self.quit)
        self.__quit_button.pack()
        self.__new_game_frame.pack()

    # Defining the event handlers
    def quit(self):
        self.__main_window.destroy()

    def instructions_window(self):
        self.__new_game_frame.destroy()

        self.__instructions_frame = Frame(self.__main_window)
        self.__Instructions_label = Label(self.__instructions_frame,
                                          text="Instructions",
                                          font=('Helvetica', 24))
        self.__Instructions_label.pack()
        rules_label=Label(self.__instructions_frame,
                          text="This Wordle game requires you to guess a word, "
                               "either 4, 5, or 6 letters, depending on your choice\n"
                               "For each word, you will have 6 attempts to guess "
                               "the word.\n"
                               "For each attempt, you will have to write the "
                               "guessing word in a line, each box containing one letter.\n"
                               "The word must be available in English, and each "
                               "box must be filled with letters, not numbers or other symbols.\n"
                               "The game will inform the warnings if these rules are not satisfied.\n"
                               "After each attempt, the ",
                          font=('Helvetica', 14))
        rules_label.pack()
        self.__return_button = Button(self.__instructions_frame,
                                      text="Return to\nmain menu",
                                      height=3, width=10,
                                      command=lambda:
                                      self.return_to_main_menu("instructions"))
        self.__return_button.pack(side=BOTTOM)
        self.__instructions_frame.pack()

    def enter_user_name(self):
        self.__new_game_frame.destroy()

        self.__enter_user_name_frame = Frame(self.__main_window)
        self.__announcement_label = Label(self.__enter_user_name_frame,
                                          text="Input your user name here",
                                          height=3, width=20)
        self.__announcement_label.pack()
        self.__input_user_name = Entry(self.__enter_user_name_frame,
                                       width=20, justify=CENTER,
                                       font=('Times', 20, 'bold'))
        self.__input_user_name.pack()
        self.__submit_button = Button(self.__enter_user_name_frame,
                                      text="Submit", height=3,
                                      command=self.store_user_name)
        self.__submit_button.pack()
        self.__enter_user_name_frame.pack()

    def store_user_name(self):
        self.__user_name = self.__input_user_name.get()
        self.New_Game_window()

    def New_Game_window(self):
        self.__enter_user_name_frame.destroy()

        self.__New_Game_window = Frame(self.__main_window)
        self.__game_label = Label(self.__New_Game_window,
                                  text="Choose the number of letters"
                                       "\nyou want to play",
                                  font=('Helvetica', 24))
        self.__game_label.pack()

        self.__4_letters_button = Button(self.__New_Game_window,
                                         text="4 letters", height=3, width=10,
                                         command=lambda: self.Start_window(4))
        self.__4_letters_button.pack()
        self.__5_letters_button = Button(self.__New_Game_window,
                                         text="5 letters", height=3, width=10,
                                         command=lambda: self.Start_window(5))
        self.__5_letters_button.pack()
        self.__6_letters_button = Button(self.__New_Game_window,
                                         text="6 letters", height=3, width=10,
                                         command=lambda: self.Start_window(6))
        self.__6_letters_button.pack()

        self.__return_button = Button(self.__New_Game_window,
                                      text="Return to\nmain menu",
                                      height=3, width=10,
                                      command=lambda:
                                      self.return_to_main_menu("new_game_window"))
        self.__return_button.pack()
        self.__New_Game_window.pack()

    def return_to_main_menu(self, frame):
        if frame == "main_game_window":
            self.__comfirmation_return_window.destroy()
            self.__Start_window.destroy()
        elif frame == "new_game_window":
            self.__New_Game_window.destroy()
        elif frame == "leaderboard":
            self.__leaderboard_frame.destroy()
        elif frame == "instructions":
            self.__instructions_frame.destroy()
        self.__main_window.update()
        self.main_menu()

    def Confirmation_return(self):
        self.__comfirmation_return_window = Toplevel()
        self.__comfirmation_return_window.geometry("500x200")
        self.__comfirmation_window_label = Label(self.__comfirmation_return_window,
                                                 text="Do you want to quit "
                                                      "this game\nand return to"
                                                      " the main menu?",
                                                 font=('Helvetica', 24))
        self.__comfirmation_window_label.pack()
        self.__yes_button = Button(self.__comfirmation_return_window,
                                   text="Yes", height=3, width=10,
                                   command=lambda: self.return_to_main_menu(
                                       "main_game_window"))
        self.__no_button = Button(self.__comfirmation_return_window,
                                  text="No", height=3, width=10,
                                  command=lambda:
                                  self.__comfirmation_return_window.destroy())
        self.__yes_button.pack()
        self.__no_button.pack()

    def Start_window(self, num):
        self.__New_Game_window.destroy()

        self.__Start_window = Frame(self.__main_window)
        title = "Wordle! " + str(num) + " letters game"
        self.__Start_window_label = Label(self.__Start_window,
                                          text=title, font=('Helvetica', 24))
        self.__Start_window_label.pack()

        self.__announcement_label = Label(self.__Start_window,
                                          text="Let's start the game!",
                                          height=6, width=30)
        self.__announcement_label.pack()

        file_name = str("dictionary_" + str(num) + "_letters.txt")
        self.__words = [line.strip() for line in open(file_name, mode="r", encoding="utf-8")]
        self.__word_to_guess = random.choice(self.__words)

        self.__entry_frame = Frame(self.__Start_window)
        self.__list_of_entries = []
        for k in range(0, 6):
            entries_in_a_row = []
            for i in range(0, num):
                self.__input_box = Entry(self.__entry_frame, width=5,
                                         justify=CENTER, font=('Times', 20, 'bold'))
                self.__input_box.grid(row=k, column=i, sticky="nsew")
                if k > 0:
                    self.__input_box.config(state='disabled')
                entries_in_a_row.append(self.__input_box)
            self.__list_of_entries.append(entries_in_a_row)
        self.__entry_frame.pack()

        self.__attempt_no = 0

        self.__submit_button = Button(self.__Start_window, text="Submit", height=3,
                                      command=lambda: self.submit_answer(self.__attempt_no))
        self.__submit_button.pack(side=LEFT)
        self.__return_button = Button(self.__Start_window, text="Return",
                                      height=3, command=self.Confirmation_return)
        self.__return_button.pack(side=LEFT)

        # Timing feature
        self.__start_time = time.time()
        self.__time_label = Label(self.__Start_window,
                                  text="Time: 0.00 seconds",
                                  font=('Helvetica', 16))
        self.__time_label.pack()

        self.__Start_window.pack()

        self.update_time()

    def submit_answer(self, attempt_no):
        correct_letters = 0
        letter_guessed = ''

        for i in range(len(self.__list_of_entries[attempt_no])):
            character = self.__list_of_entries[attempt_no][i].get()
            if len(character) > 1:
                self.__announcement_label.config(text="Error, each box must "
                                                      "contain\n1 character "
                                                      "only!")
                return
            elif len(character) != 1:
                self.__announcement_label.config(
                    text="Error, all letter boxes must be filled!")
                return
            elif not (97 <= ord(character.lower()) <= 122):
                self.__announcement_label.config(
                    text="Error, only letters are allowed!")
                return
            letter_guessed += character.lower()

        if letter_guessed not in self.__words:
            self.__announcement_label.config(
                text="Error, the word you guessed \n "
                     "is not available in English!")
            return

        for i in range(len(self.__list_of_entries[attempt_no])):
            for k in range(len(self.__list_of_entries[attempt_no])):
                character = self.__list_of_entries[attempt_no][i].get()
                if character.lower() == self.__word_to_guess[k]:
                    if i == k:
                        self.__list_of_entries[attempt_no][i].config(
                            {"background": "green"})
                        correct_letters += 1
                        pass
                    else:
                        self.__list_of_entries[attempt_no][i].config(
                            {"background": "orange"})

        if correct_letters == len(self.__list_of_entries[attempt_no]):
            self.__announcement_label.config(
                text="Congratulations! \n "
                     "You have figured out the right word \n with " + str(
                    attempt_no + 1) + " attempts!")

            # Calculate and display the time taken
            end_time = time.time()
            time_taken = end_time - self.__start_time
            self.__end_time = end_time  # Store the end time
            self.__announcement_label.config(
                text=self.__announcement_label.cget("text") +
                     "\nTime Taken: {:.2f} seconds".format(time_taken))

            self.__submit_button.config(state='disabled')

            # Add the score to the leaderboard
            self.add_to_leaderboard(self.__user_name,
                                    len(self.__list_of_entries[attempt_no]),
                                    attempt_no+1,
                                    time_taken)

            return

        if attempt_no == 4:
            self.__announcement_label.config(text="Attempt 5 finished!\nLast try!")
        elif attempt_no == 5:
            self.__announcement_label.config(
                text="Attempt 6 finished!\nGame over!\nThe correct letter is " + self.__word_to_guess)
            self.__submit_button.config(state='disabled')
            self.__end_time = time.time()  # Stop the timer
            return
        else:
            self.__announcement_label.config(text="Attempt " +
                                                  str(attempt_no + 1) +
                                                  " finished!")

        self.__attempt_no += 1
        for i in range(len(self.__list_of_entries[attempt_no + 1])):
            self.__list_of_entries[attempt_no + 1][i].configure(state='normal')

    def update_time(self):
        if not self.__time_label.winfo_exists():
            return
        current_time = 0
        if self.__start_time and not self.__end_time:
            current_time = time.time() - self.__start_time
        elif self.__end_time:
            current_time = self.__end_time - self.__start_time
        self.__time_label.config(text="Time: {:.2f} seconds".format(current_time))
        self.__main_window.after(100, self.update_time)

    def leaderboard_window_display(self):
        self.__new_game_frame.destroy()

        self.__leaderboard_frame = Frame(self.__main_window)
        self.__leaderboard_frame.pack()

        # Title label
        title_label = Label(self.__leaderboard_frame, text="Leaderboard",
                            font=('Helvetica', 24, 'bold'))
        title_label.grid(row=0, column=20, columnspan=3, pady=10)

        leaderboard_entries = self.get_leaderboard_entries()

        # Sort leaderboard entries based on time_taken in ascending order
        leaderboard_entries.sort(key=lambda x: x['time_taken'])
        leaderboard_entries.sort(key=lambda x: x['attempts'])

        # Display only the top 10 entries
        num_entries_to_display = min(len(leaderboard_entries), 10)



        for i in range(num_entries_to_display):
            entry = leaderboard_entries[i]

            # Rank label
            rank_label = Label(self.__leaderboard_frame,
                               text="{}. ".format(i + 1),
                               font=('Helvetica', 16))
            rank_label.grid(row=i + 1, column=1, padx=(10, 0), pady=5,
                            sticky=W)

            # User label
            user_label = Label(self.__leaderboard_frame,
                               text="User: {}".format(entry['user_name']),
                               font=('Helvetica', 16))
            user_label.grid(row=i + 1, column=6, pady=5, sticky=W)

            # Letters label
            letters_label = Label(self.__leaderboard_frame,
                                  text="Letters: {}".format(
                                      entry['num_letters']),
                                  font=('Helvetica', 16))
            letters_label.grid(row=i + 1, column=16, pady=5, sticky=W)

            # Letters label
            attempts_label = Label(self.__leaderboard_frame,
                                  text="Attempts: {}".format(
                                      entry['attempts']),
                                  font=('Helvetica', 16))
            attempts_label.grid(row=i + 1, column=21, pady=5, sticky=W)

            # Time label
            time_label = Label(self.__leaderboard_frame,
                               text="Time: {:.2f} seconds".format(
                                   entry['time_taken']),
                               font=('Helvetica', 16))
            time_label.grid(row=i + 1, column=29, padx=(0, 10), pady=5,
                            sticky=W)

        return_button = Button(self.__leaderboard_frame,
                               text="Return to\nmain menu",
                               height=3, width=10,
                               command=lambda: self.return_to_main_menu(
                                   "leaderboard"))
        return_button.grid(row=num_entries_to_display + 2, column=20,
                           columnspan=4, pady=10)

    def get_leaderboard_entries(self):
        leaderboard_entries = []
        try:
            with open('leaderboard.txt', 'r') as file:
                for line in file:
                    entry_data = line.strip().split(';')
                    if len(entry_data) == 4:
                        leaderboard_entry = {
                            'user_name': entry_data[0],
                            'num_letters': int(entry_data[1]),
                            'attempts': int(entry_data[2]),
                            'time_taken': float(entry_data[3])
                        }
                        leaderboard_entries.append(leaderboard_entry)
        except FileNotFoundError:
            pass
        return leaderboard_entries

    def add_to_leaderboard(self, user_name, num_letters, attempts, time_taken):
        leaderboard_entry = "{};{};{};{:.2f}".format(user_name, num_letters,
                                                     attempts, time_taken)
        try:
            with open('leaderboard.txt', 'a') as file:
                file.write(leaderboard_entry + '\n')
        except FileNotFoundError:
            pass


def main():
    gui = GUI()


if __name__ == "__main__":
    main()