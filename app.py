import numpy as np
import math
from customtkinter import CTk, CTkButton, set_appearance_mode, set_default_color_theme
from PIL import Image, ImageTk
import tkinter as tk

def update_ucbs(Ni, Ri, round):
    ads = len(Ni)
    maxUCB = 0
    ad = 0
    for i in range(ads):
        if Ni[i] > 0:
            avgReward = Ri[i] / Ni[i]
            error = math.sqrt((3 / 2) * (math.log(round + 1) / Ni[i]))
            LCB = avgReward - error
            UCB = avgReward + error
        else:
            UCB = 1e400

        if UCB > maxUCB:
            maxUCB = UCB
            ad = i
    return ad

def select_ad_feedback():
    global round, Ni, Ri, total_rewards, threshold
    feedback = 1
    ad = update_ucbs(Ni, Ri, round)
    ads_selected.append(ad)
    Ni[ad] += 1
    Ri[ad] += feedback
    total_rewards += feedback
    print(f"Total rewards after round {round + 1}: {total_rewards}")
    if Ni[np.argmax(Ni)] > threshold:
        print(f"The most clicked ad is ad {np.argmax(Ni) + 1}. Stopping after {round + 1} rounds.")
        update_ui()
        return
    update_ui()

def skip_ad_feedback():
    global round, Ni, Ri, total_rewards, threshold
    feedback = 0
    ad = update_ucbs(Ni, Ri, round)
    ads_selected.append(-1)  # Indicates a skip
    Ni[ad] += 1
    Ri[ad] += feedback
    total_rewards += feedback
    print(f"Total rewards after round {round + 1}: {total_rewards}")
    if Ni[np.argmax(Ni)] > threshold:
        print(f"The most clicked ad is ad {np.argmax(Ni) + 1}. Stopping after {round + 1} rounds.")
        update_ui()
        return
    update_ui()

def update_ui():
    global round, Ni, Ri, total_rewards, threshold, select_button, skip_button, ad_label, ad_image_label, ad_images

    round += 1
    ad = update_ucbs(Ni, Ri, round)

    ad_label.configure(text=f"Feedback for ad {ad + 1}:")
    ad_image_label.configure(image=ad_images[ad])

    select_button.configure(command=select_ad_feedback)
    skip_button.configure(command=skip_ad_feedback)

def main():
    global round, Ni, Ri, total_rewards, threshold, ads_selected, ad_label, select_button, skip_button, ad_image_label, ad_images

    n = 1000  # total number of rounds
    ads = 10  # total number of ads
    Ni = np.zeros(ads, dtype=int)
    Ri = np.zeros(ads, dtype=int)
    ads_selected = []
    total_rewards = 0
    threshold = n * 0.02

    round = 0

    set_appearance_mode("dark")
    set_default_color_theme("dark-blue")

    app = CTk()
    app.geometry("600x500")
    app.title("Advertisement Optimizer")

    heading_label = tk.Label(app, text="Advertisement Optimizer", font=("Arial", 30, "bold"))
    heading_label.pack(pady=10)

    ad_label = tk.Label(app, text="", font=("Arial", 14))
    ad_label.pack(pady=10)

    ad_images = []
    for i in range(1, ads + 1):
        img = Image.open(f"src/img ({i}).jpg")
        img = img.resize((200, 200))  # Resize image if needed
        img = ImageTk.PhotoImage(img)
        ad_images.append(img)

    ad_image_label = tk.Label(app, image=ad_images[0])
    ad_image_label.pack()

    button_frame = tk.Frame(app)
    button_frame.pack(pady=20)

    skip_button = CTkButton(button_frame, text="Skip", command=skip_ad_feedback, width=10)
    skip_button.pack(side=tk.LEFT, padx=20, pady=10)

    select_button = CTkButton(button_frame, text="Select", command=select_ad_feedback, width=10)
    select_button.pack(side=tk.LEFT, padx=20, pady=10)

    update_ui()

    app.mainloop()

if __name__ == "__main__":
    main()
