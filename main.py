import tkinter as tk
from PIL import Image, ImageTk
import os
import random

class ImageSwitcher(tk.Tk):
    def __init__(self, image_folder):
        super().__init__()

        self.image_folder = image_folder
        self.image_paths = [os.path.join(image_folder, file) for file in os.listdir(image_folder)]
        random.shuffle(self.image_paths)

        self.current_indexes = [0, 0, 0]
        self.paused = False
        self.count = 0
        self.first = True
        self.button_pressed = False  # 表示按钮是否被按下

        self.canvas1 = tk.Canvas(self, width=200, height=200)
        self.canvas1.pack(side=tk.LEFT)

        self.canvas2 = tk.Canvas(self, width=200, height=200)
        self.canvas2.pack(side=tk.LEFT)

        self.canvas3 = tk.Canvas(self, width=200, height=200)
        self.canvas3.pack(side=tk.LEFT)

        self.canvas4 = tk.Canvas(self, width=200, height=200)
        self.canvas4.pack(side=tk.LEFT)

        self.load_images()

        self.button_pause = tk.Button(self, text="Click", command=self.toggle_pause)
        self.button_pause.pack()

    def load_images(self):
        for i in range(3):
            if 0 <= self.current_indexes[i] < len(self.image_paths):
                image_path = self.image_paths[self.current_indexes[i]]
                image = Image.open(image_path)
                resized_image = image.resize((200, 200))
                tk_image = ImageTk.PhotoImage(resized_image)
                getattr(self, f'canvas{i+1}').create_image(0, 0, anchor=tk.NW, image=tk_image)
                getattr(self, f'canvas{i+1}').image = tk_image  # 保持對圖片的引用

    def show_next_images(self, i, t):
        if not self.paused and self.button_pressed:
            getattr(self, f'canvas{4}').delete("all")
            if 0 <= self.current_indexes[i] < len(self.image_paths):
                self.current_indexes[i] += 1
                if self.current_indexes[i] >= len(self.image_paths):
                    self.current_indexes[i] = 0
                self.load_images()
        self.after(t, lambda: self.show_next_images(i, t))

    def toggle_pause(self):
        if self.first:
            random.shuffle(self.image_paths)
            self.current_indexes = [0, 0, 0]
            self.paused = False
            self.show_next_images(0, 50)
            self.show_next_images(1, 100)
            self.show_next_images(2, 150)
            self.first = False
        else:
            self.button_pressed = not self.button_pressed  # 切换按扭
            self.show_reward()

    def show_reward(self):
        image_path1 = self.image_paths[self.current_indexes[0]]
        image_path2 = self.image_paths[self.current_indexes[1]]
        image_path3 = self.image_paths[self.current_indexes[2]]
        print(image_path1)
        print(image_path2)
        print(image_path3)
        print(self.count)
        print("----------")
        unique_paths = {image_path1, image_path2, image_path3}
        if len(unique_paths) == 1:
            image_path = "D:/OS/reward/a.gif"
        elif len(unique_paths) == 2:
            self.count += 1
            image_path = "D:/OS/reward/b.gif"
        else:
            self.count += 1
            image_path = "D:/OS/reward/c.gif"

        resized_image = Image.open(image_path).resize((200, 200))
        tk_image = ImageTk.PhotoImage(resized_image)
        getattr(self, f'canvas{4}').create_image(0, 0, anchor=tk.NW, image=tk_image)
        getattr(self, f'canvas{4}').image = tk_image

        if (self.count % 3) == 0:
            image_path = self.image_paths[self.current_indexes[0]]
            resized_image = Image.open(image_path).resize((200, 200))
            tk_image = ImageTk.PhotoImage(resized_image)

            for i in range(1, 4):
                getattr(self, f'canvas{i}').delete("all")  # 清空 Canvas 上的內容
                getattr(self, f'canvas{i}').create_image(0, 0, anchor=tk.NW, image=tk_image)
                getattr(self, f'canvas{i}').image = tk_image

            reward_path = "D:/OS/reward/a.gif"
            resized_image = Image.open(reward_path).resize((200, 200))
            tk_image = ImageTk.PhotoImage(resized_image)
            getattr(self, f'canvas{4}').delete("all")  # 清空 Canvas 上的內容
            getattr(self, f'canvas{4}').create_image(0, 0, anchor=tk.NW, image=tk_image)
            getattr(self, f'canvas{4}').image = tk_image


if __name__ == "__main__":
    image_folder = "D:/OS/pic"
    app = ImageSwitcher(image_folder)
    app.mainloop()
