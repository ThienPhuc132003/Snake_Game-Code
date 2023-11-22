import tkinter
from tkinter import *
import random
from tkinter import font
from turtle import window_height, window_width
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from time import sleep
from tkinter import simpledialog, messagebox
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456Phuc@",
    database="LeaderBoard"
)

window = Tk()
window.title("Snake Game Python")
window.resizable(0,0)

Label(window, text='ENTERTAINMENT', font='arial 20 bold').pack(side=BOTTOM)

score = 0
direction = 'down'

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED= 180
SPACE_SIZE = 50
BODY_PARTS = 2
SNAKE_COLOR = '#00FF00'
SNAKE_COLOR1 = '#ff8c00'
SNAKE_COLOR2= "#ffff1a"
FOOD_COLOR = '#FF0000'
BACKGROUND_COLOR = '#000000'


class ToolTip(object):
    def __init__(self, widget, tip_text=None):
        self.widget = widget
        self.tip_text = tip_text
        widget.bind("<Enter>", self.mouse_enter)
        widget.bind("<Leave>", self.mouse_leave)
    
    def mouse_enter(self, _event):
        self.show_tooltip()

    def mouse_leave(self, _event):
        self.hide_tooltip()

    def show_tooltip(self):
        if not hasattr(self, "tip_window"):
            x_left = self.widget.winfo_rootx()
            y_top = self.widget.winfo_rooty() - 18
            self.tip_window = tk.Toplevel(self.widget)
            # Loại bỏ khung viền, và trang trí
            self.tip_window.overrideredirect(True)
            self.tip_window.geometry("+%d+%d" % (x_left, y_top))
            label = ttk.Label(self.tip_window, text=self.tip_text, relief= tk.SOLID, background= "#ffffe0", justify=tk.LEFT, borderwidth=1, font=("tahoma", "8", "normal"))
            label.pack()
    
    def hide_tooltip(self):
        if hasattr(self, "tip_window"):
            self.tip_window.destroy()
            del self.tip_window

# Bind the 'B' key to change the background color
def change_background_color():
    global BACKGROUND_COLOR
    colors = [ '#F8DC90', '#AEC289', '#2F9091', '#107C93', '#000000']
    # Cycle through different background colors
    current_color_index = colors.index(BACKGROUND_COLOR)
    next_color_index = (current_color_index + 1) % len(colors)
    BACKGROUND_COLOR = colors[next_color_index]
    canvas.configure(bg=BACKGROUND_COLOR)
window.bind('b', lambda event: change_background_color())
# Create the color change button.
change_color_button = tk.Button(window, text="Change Color", command=change_background_color)
ToolTip(change_color_button, "This is change color button")
# Place the color change button next to the score label.
change_color_button.pack(side=tk.TOP, padx=10)

#####################################################################
# Tạo hàm để reset trò chơi
def reset_game():
    global score, direction
    score = 0
    label.config(text="Score: {}".format(score))
    direction = 'down'
    canvas.delete("snake", "food")
    canvas.delete('gameover')
    snake.__init__()
    food.__init__()
    next_turn(snake, food)
      

# Tạo nút "Reset" và thêm Tooltip cho nó
reset_button = tk.Button(window, text="Reset", command=reset_game)
ToolTip(reset_button, "Reset Game")
reset_button.pack(side=tk.TOP, padx=10)

#######################################################################
player_name = ""
player_score = 0
highscore=[]
leaderboard = []
leaderboard_data=[]
mycursor = mydb.cursor()
# Nhập tên người chơi
def get_player_name():
    global player_name
    player_name = simpledialog.askstring("Enter Your Name", "Enter your name:")
def save_score():
    sqlFormula="INSERT INTO highscore(name,score) VALUES (%s,%s)"
    mycursor.executemany(sqlFormula,highscore)
    mydb.commit()
def show_leaderboard():
    leaderboard_window = Tk()
    leaderboard_window.title("Leaderboard")
    mycursor.execute("SELECT * FROM highscore")
    myresult = mycursor.fetchall()
    leaderboard_data.extend(myresult)

    # Sort the leaderboard_data by score from high to low
    leaderboard_data.sort(key=lambda x: x[1], reverse=True)

    # Tạo một Label để hiển thị tiêu đề
    leaderboard_title_label = Label(leaderboard_window, text="Leaderboard", font=('consolas', 20))
    leaderboard_title_label.pack()

    # Tạo một Frame để chứa danh sách điểm
    leaderboard_frame = Frame(leaderboard_window)
    leaderboard_frame.pack()

    # Tạo Label và hiển thị danh sách điểm
    player_label = Label(leaderboard_frame, text="Name", font=('consolas', 12, 'bold'))
    player_label.grid(row=0, column=0, padx=10)
    
    score_label = Label(leaderboard_frame, text="Score", font=('consolas', 12, 'bold'))
    score_label.grid(row=0, column=1, padx=10)

    # Concatenate data for each player into a string and set as the text for player_label
    for idx, player_data in enumerate(leaderboard_data, start=1):
        player_info = f"{player_data[0]}"
        score_info = f"{player_data[1]}"
        
        Label(leaderboard_frame, text=player_info, font=('consolas', 12)).grid(row=idx, column=0, padx=10)
        Label(leaderboard_frame, text=score_info, font=('consolas', 12)).grid(row=idx, column=1, padx=10)
ShowLeaderBoard_button = tk.Button(window, text="LeaderBoard", command=show_leaderboard)
ToolTip(ShowLeaderBoard_button, "This is LeaderBoard")
ShowLeaderBoard_button.pack(side=tk.TOP, padx=10)
#########################################################################

#EXIT GUI cleanly
def _quit():
    window.quit()
    window.destroy()
    exit()
def open_new_window():
    # Create a new window
    new_window = tk.Toplevel(root)
    # Set the title of the new window
    new_window.title("Hướng dẫn chơi")
    ttk.Label(new_window,text="Sử dụng dấu mũi tên trên bàn phím để di chuyển").grid(column=0,row=0)
    ttk.Label(new_window,text=" ⇢ là đi sang phải ").grid(column=0,row=1,sticky=W)
    ttk.Label(new_window,text=" ⇠ là đi sang trái ").grid(column=0,row=2,sticky=W)
    ttk.Label(new_window,text=" ⇣ là đi xuống dưới ").grid(column=0,row=3,sticky=W)
    ttk.Label(new_window,text=" ⇡ là đi lên trên ").grid(column=0,row=4,sticky=W)
    ttk.Label(new_window,text="Nút Change color dùng để đổi màu nền game").grid(column=0,row=5,sticky=W)
    ttk.Label(new_window,text="Nút reset dùng để reset lại game khi kết thúc game").grid(column=0,row=6,sticky=W)
    ttk.Label(new_window,text="Nút LeaderBoard hiển thị số điểm cao nhất").grid(column=0,row=7,sticky=W)
    
    # Pack the new window
    new_window.pack()
def open_new_window2():
    # Create a new window
    new_window2 = tk.Toplevel(root)
    # Set the title of the new window
    new_window2.title("Hướng dẫn chơi")
    ttk.Label(new_window2,text="Game được viết bởi 3 thành viên gồm:\nĐỗ Tùng Lâm\nĐặng Phương Nam\nTrịnh Văn Thiên Phúc").grid(column=0,row=0)
    ttk.Label(new_window2,text="!!!Điều khiển con rắn của bạn ăn thức ăn để được số điểm cao nhất!!!").grid(column=0,row=1)
    
    # Pack the new window
    new_window2.pack()
    
root = window
label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas2=Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()


# Create a boolean variable to track whether the game is started or not
game_started = False

# Function to handle mouse click to start the game
def start_game(event):
    global game_started
    if not game_started:
        game_started = True
        canvas.delete("start_screen")  # Remove the start screen
        next_turn(snake, food)  # Start the game

# Create a "Click to Start" screen
start_screen_text = canvas.create_text(
    GAME_WIDTH / 2,
    GAME_HEIGHT / 2,
    text="Click to Start",
    font=("consolas", 40),
    fill="white",
    tags="start_screen"
)

# Bind the mouse click event to the start_game function
canvas.bind("<Button-1>", start_game)


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y +SPACE_SIZE, fill= SNAKE_COLOR, tag ="snake")
            self.squares.append(square)
    def change_color(self):
        for square in self.squares:
            canvas.itemconfig(square, fill=SNAKE_COLOR1)

class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1)*SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE

        self.coordinates = [x,y]
        canvas.create_oval(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tag='food')

def next_turn(snake, food):
    global score
    x, y = snake.coordinates[0]

    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction =='right':
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x,y))
    if score >= 5:
        square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR1)
    else:
        square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0,square)


    if x == food.coordinates[0] and y == food.coordinates[1]:
        #global score

        score += 1
        label.config(text='Score:{}'.format(score))
        canvas.delete("food")
        food = Food()
        if score >= 5:
            snake.change_color()
        
    else:
        del snake.coordinates[-1]
        canvas .delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    if new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    if new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    if new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):
    x,y = snake.coordinates[0]
    if x<0 or x>=GAME_WIDTH:
        return True
    
    elif y<0 or y>= GAME_HEIGHT:
        return True
    
    for body_part in snake.coordinates[1:]:
        if x== body_part[0] and y == body_part[1]:
            return True
        
    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,
    canvas.winfo_height()/2,
    font=('consolas', 70),
    text = 'GAME OVER',
    fill= 'red',
    tag='gameover')
    get_player_name()
    player_score = score
    highscore.append((player_name, player_score))
    save_score()
    show_leaderboard()
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2)-(window_width/2))
y = int((screen_height/2)-(window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()
#Creating a Menu_Bar
menu_bar = Menu(window)
window.config(menu=menu_bar)
#Create menu and add menu items
#tear something off
file_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File",menu = file_menu)
file_menu.add_command(label="New",command=reset_game)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=_quit)
file_menu.add_separator()
#Tip
menu_bar.add_cascade(label="Tip", command=open_new_window)
#about
menu_bar.add_cascade(label="About", command=open_new_window2)    



window.mainloop()