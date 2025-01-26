import tkinter
import customtkinter
from tkinter import filedialog,colorchooser
import tkinter.messagebox as tsmg
from PIL import Image,ImageTk,ImageFilter,ImageDraw,ImageFont,ImageGrab
import numpy as np
import re

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# functions
def help():
  tsmg.showinfo("HELP","To know how to use it please reach our webpage \n www.AnupamChitraEditor.com")

def about():
  tsmg.showinfo("ABOUT","It is a simple yet very useful offline image editor with numerous features like filters, crop, drawing,etc")

# displaying the images
def displayimage(img):
  workarea.icon=ImageTk.PhotoImage(img)
  workarea.itemconfigure(image_id,image=workarea.icon)

# drawing on image
##############
def stoping_to_draw():
  workarea.unbind("<Button-1>")
  workarea.unbind("<B1-Motion>")# TO STOP ALL DRAWING ON THE CANVAS OR WORKAREA
  workarea.unbind("<ButtonRelease-1>")

def draw():
  workarea.bind("<Button-1>",get_x_and_y)
  workarea.bind("<B1-Motion>",paint)

  
def get_x_and_y(event):
  global lasx,lasy
  lasx,lasy=event.x,event.y

def paint(event):
  global line
  global lasx,lasy
  line=workarea.create_line((lasx,lasy,event.x,event.y),fill=current_color,width=round(brush_slider.get(),1))
  lasx=event.x
  lasy=event.y

def choose_color():
  global current_color
  _,current_color=colorchooser.askcolor(title="Choose Color")# since tupl with rgb code first and then hex code
  colorchooser_b_l.configure(bg=current_color,fg=current_color)
  colorchooser_b_l_d.configure(bg=current_color,fg=current_color)

def clear():
  global img,icon,image_id
  workarea.delete("all")
  icon=Image.open("logo/workarea_image_icon.png")
  icon=ImageTk.PhotoImage(icon)
  workarea.create_image(0,0,image=icon,anchor="nw")
  image_id=workarea.create_image(0,0, anchor="nw")
  displayimage(img)


  # making the reset button
#######################
def reset_():
  global img,icon,image_id
  workarea.delete("all")
  icon=Image.open("logo/workarea_image_icon.png")
  icon=ImageTk.PhotoImage(icon)
  workarea.create_image(0,0,image=icon,anchor="nw")
  image_id=workarea.create_image(0,0, anchor="nw")
  img=imgname
  img = Image.open(imgname).convert('RGB')
  h=workarea_set_heightentry
  w=workarea_set_widthentry
  img = img.resize((w,h))
  displayimage(img)
  stoping_to_draw()
  bri_sli.set(0)
  cat_sli.set(0)
  sat_sli.set(0)
  gamma_sli.set(1)
  blur_sli.set(0)
  bri_sli_label.configure(text="0")
  cat_sli_label.configure(text="0")
  sat_sli_label.configure(text="0")
  blur_sli_label.configure(text="0")
  gamma_sli_label.configure(text="1")

#showing the size of image
##################
def size_details():
  imgname_=Image.open(imgname)
  size_values=f"{imgname_.size[0]}x{imgname_.size[1]}"
  size_detail.configure(text=size_values)
  
# opening the images
###########
def openimage():
  global img,imgname
  filetypes = (('JPG', '*.jpg'),('PNG', '*.png'),('JPEG','*.jpeg'),('GIF','*.gif'),('Bitmap','*.bmp'),('PPM','*.ppm'),('All Types','*.*'))
  imgname =tkinter.filedialog.askopenfilename (title="open",filetypes=filetypes)
  if imgname:
    img = Image.open(imgname).convert('RGB')
    h=workarea_set_heightentry
    w=workarea_set_widthentry
    img = img.resize((w,h))
    displayimage(img)
  stoping_to_draw()
  size_details()

# resizing the image
##################
def resize_():
  global img
  img=img.resize((widthvalue.get(),heightvalue.get()))
  displayimage(img)
  stoping_to_draw()

# flipping the images
###########
def flip_lr():
   global img
   img = img.transpose(Image.FLIP_LEFT_RIGHT)
   displayimage(img)
   stoping_to_draw()

############
def flip_tb():
   global img
   img = img.transpose(Image.FLIP_TOP_BOTTOM)
   displayimage(img)
   stoping_to_draw()
  
#rotating the images
##########
def rotate_():
  global img
  img = img.transpose(Image.ROTATE_90)
  displayimage(img)
  stoping_to_draw()

  # filters
  ############
def emboss():
  global img
  img=img.filter(ImageFilter.EMBOSS)
  displayimage(img)
  stoping_to_draw()

##############
def contour():
  global img
  img=img.filter(ImageFilter.CONTOUR)
  displayimage(img)
  stoping_to_draw()

#############
def gray():
  global img
  img=img.convert('L')
  displayimage(img) 
  stoping_to_draw()

######################
def fedges():
  global img
  img=img.filter(ImageFilter.FIND_EDGES)
  displayimage(img)
  stoping_to_draw()

def detail_filter():
  global img
  img=img.filter(ImageFilter.DETAIL)
  displayimage(img)
  stoping_to_draw()
  
#########
def warm():
  global img
  img=img.convert('RGB')
  for i in range(0, img.size[0]-1):
    for j in range(0, img.size[1]-1):
      # Get pixel value at (x,y) position of the image
      pixelColorVals = img.getpixel((i,j))
      # Invert color
      redPixel    = int(pixelColorVals[0]*1.1) # 
      greenPixel  = pixelColorVals[1] # 
      bluePixel   = int(pixelColorVals[2]/1.5) # 
      
      img.putpixel((i,j),(redPixel, greenPixel, bluePixel))
  displayimage(img)
  stoping_to_draw()
def cool():
  global img
  img=img.convert('RGB')
  for i in range(0, img.size[0]-1):
    for j in range(0, img.size[1]-1):
      # Get pixel value at (x,y) position of the image
      pixelColorVals = img.getpixel((i,j))
      # Invert color
      redPixel    = int(pixelColorVals[0]/1.5) # Negate red pixel
      greenPixel  = pixelColorVals[1] # Negate green pixel
      bluePixel   = int(pixelColorVals[2]*1.2) # Negate blue pixel
      # Modify the image with the inverted pixel values
      img.putpixel((i,j),(redPixel, greenPixel, bluePixel))
  displayimage(img)
  stoping_to_draw()
def sketch():
  global img
  img=img.convert('L')
  for i in range(0,img.size[0]-1):
    for j in range(0,img.size[1]-1):
      pixelColorVals = img.getpixel((i,j))
      whitepixel=255-pixelColorVals
      img.putpixel((i,j),whitepixel)
  img=img.filter(ImageFilter.CONTOUR)
      
  displayimage(img)
  stoping_to_draw()

#######
def negative():
  global img
  img=img.convert('RGB')
  for i in range(0, img.size[0]-1):
    for j in range(0, img.size[1]-1):
      # Get pixel value at (x,y) position of the image
      pixelColorVals = img.getpixel((i,j))
      # Invert color
      redPixel    = 255 - pixelColorVals[0] # Negate red pixel
      greenPixel  = 255 - pixelColorVals[1] # Negate green pixel
      bluePixel   = 255 - pixelColorVals[2] # Negate blue pixel
      # Modify the image with the inverted pixel values
      img.putpixel((i,j),(redPixel, greenPixel, bluePixel))
  displayimage(img)
  stoping_to_draw()

# sepai
#########
def sepai():
  def get_max(value):
    if value > 255:
        return 255
    return int(value)
  # Get size
  global img
  width, height = img.size

  # Create new Image and a Pixel Map
  new = Image.new("RGB", (width, height), "white")

  # Convert each pixel to sepia
  for i in range(0, width, 1):
    for j in range(0, height, 1):
      if i > width or j > height:
          return None
  
      # Get Pixel
      pixel = img.getpixel((i, j))
      red=pixel[0]
      green=pixel[1]
      blue=pixel[2]
      value = 0
      alpha=255
      # This is a really popular implementation
      tRed = get_max((0.759 * red) + (0.398 * green) + (0.194 * blue))
      tGreen = get_max((0.676 * red) + (0.354 * green) + (0.173 * blue))
      tBlue = get_max((0.524 * red) + (0.277 * green) + (0.136 * blue))
  
      if value == 1:
        tRed = get_max((0.759 * red) + (0.398 * green) + (0.194 * blue))
        tGreen = get_max((0.524 * red) + (0.277 * green) + (0.136 * blue))
        tBlue = get_max((0.676 * red) + (0.354 * green) + (0.173 * blue))
      if value == 2:
        tRed = get_max((0.676 * red) + (0.354 * green) + (0.173 * blue))
        tGreen = get_max((0.524 * red) + (0.277 * green) + (0.136 * blue))
        tBlue = get_max((0.524 * red) + (0.277 * green) + (0.136 * blue))
      # pixels[i,j]=tRed,tGreen,tBlue,alpha dont use this otherwise clear option of draw will erase it
      new.putpixel((i,j),(tRed, tGreen, tBlue,alpha))#use this instead
  img=new
  displayimage(img)
  stoping_to_draw()

#pointilize
############
def pointilize():
  global img
  def color_average(img, i0, j0, i1, j1):
    # Colors
    red, green, blue, alpha = 0, 0, 0, 255

    # Get size
    width, height = img.size

    # Check size restrictions for width
    i_start, i_end = i0, i1
    if i0 < 0:
        i_start = 0
    if i1 > width:
        i_end = width

    # Check size restrictions for height
    j_start, j_end = j0, j1
    if j0 < 0:
        j_start = 0
    if j1 > height:
        j_end = height

    # This is a lazy approach, we discard half the pixels we are comparing
    # This will not affect the end result, but increase speed
    count = 0
    for i in range(i_start, i_end - 1, 1):
        for j in range(j_start, j_end - 1, 1):
            count+=1
            if i > width or j > height:
              return None

    # Get Pixel
            pixel = img.getpixel((i, j))
            red, green, blue = pixel[0] + red, pixel[1] + green, pixel[2] + blue

    # Set color average
    red /= count
    green /= count
    blue /= count

    # Return color average
    return int(red), int(green), int(blue), alpha
  # Get size
  width, height = img.size

  # Radius
  radius = 5

  # Intentional error on the positionning of dots to create a wave-like effect
  count = 0
  errors = [1, 0, 1, 1, 2, 3, 3, 1, 2, 1]
  new = Image.new("RGB", (width, height), "white")
  draw = ImageDraw.Draw(new)
  for i in range(0, width, radius+2):
    for j in range(0, height, radius+2):
      color = color_average(img, i-radius, j-radius, i+radius, j+radius)
      eI = errors[count % len(errors)]
      count += 1
      eJ = errors[count % len(errors)]

      # Create circle
      draw.ellipse((i-radius+eI, j-radius+eJ, i+radius+eI, j+radius+eJ), fill=(color))
  img=new# for not being cleared when clear of draw is pressed
  displayimage(img)
  stoping_to_draw()

###########edit tab 

def bright(var):
  global new_image
  bright_val=bri_sli.get()
  new_image=pre_img()
  for i in range(0,new_image.width-1):
    for j in range(0,new_image.height-1):
      pixel=img.getpixel((i,j))
      red=min(255,max(0,pixel[0]+bright_val))
      green=min(255,max(0,pixel[1]+bright_val))
      blue=min(255,max(0,pixel[2]+bright_val))
      new_image.putpixel((i,j),(int(red),int(green),int(blue)))
  displayimage(new_image)
  stoping_to_draw()
  bri_sli_label.configure(text=f"{round(bright_val,2)}")

def saturation(var):
  global new_image
  sat_val=sat_sli.get()
  beta=sat_val
  new_image=pre_img()
  if beta == 255: 
    alpha = np.infty
  else: 
    alpha = (255+beta)/(255-beta)
  for i in range(0,new_image.width-1):
    for j in range(0,new_image.height-1):
      pixel=img.getpixel((i,j))
      u=(pixel[0]+pixel[1]+pixel[2])/3
      red=min(255,max(0,alpha*(pixel[0]-u)+u))
      green=min(255,max(0,alpha*(pixel[1]-u)+u))
      blue=min(255,max(0,alpha*(pixel[2]-u)+u))
      new_image.putpixel((i,j),(int(red),int(green),int(blue)))
  displayimage(new_image)
  stoping_to_draw()
  sat_sli_label.configure(text=f"{round(sat_val,2)}")

def contrast(var):
  global new_image
  cat_val=cat_sli.get()  
  beta=cat_val
  new_image=pre_img()
  data = np.array(new_image)
  # Calculate average brightness
  u = np.mean(data, axis=2)
  u_mean = u.mean()
  # Calculate factor
  if beta == 255:
    alpha = np.infty
  else:
    alpha = (255+beta)/(255-beta)
  for i in range(0,new_image.width-1):
    for j in range(0,new_image.height-1):
      pixel=img.getpixel((i,j))
      red=min(255,max(0,alpha*(pixel[0]-u_mean)+u_mean))
      green=min(255,max(0,alpha*(pixel[1]-u_mean)+u_mean))
      blue=min(255,max(0,alpha*(pixel[2]-u_mean)+u_mean))
      new_image.putpixel((i,j),(int(red),int(green),int(blue)))
  displayimage(new_image)
  stoping_to_draw()
  cat_sli_label.configure(text=f"{round(cat_val,2)}")

def blur_(var):
  global new_image
  kernel_size=blur_sli.get()  
  new_image=pre_img()
  data = np.array(new_image)
  a = kernel_size // 2
  for i in range(0, new_image.size[0]-1):
    for j in range(0, new_image.size[1]-1):
      x_start=int(max(i-a,0))
      y_start=int(max(j-a,0))
      x_end=int(min(i+a+1,img.size[0]-1))
      y_end=int(min(j+a+1,img.size[1]-1))
      square = data[y_start:y_end, x_start:x_end]
      # Invert color
      redPixel,greenPixel,bluePixel =square.mean(axis=(0,1)) # Negate red pixel
      # Modify the image with the inverted pixel values
      new_image.putpixel((i,j),(int(redPixel), int(greenPixel), int(bluePixel)))
  displayimage(new_image)
  blur_sli_label.configure(text=f"{round(kernel_size,2)}")
  stoping_to_draw()

def gamma(var):
  global new_image
  gammaval=round(gamma_sli.get(),2)
  new_image=pre_img()
  new_image=new_image.convert('RGB')
  for i in range(0, new_image.size[0]-1):
    for j in range(0, new_image.size[1]-1):
      # Get pixel value at (x,y) position of the image
      pixelColorVals = new_image.getpixel((i,j))
      # Invert color
      redPixel    = int(255*(pixelColorVals[0]/255)**gammaval) # Negate red pixel
      greenPixel  = int(255*(pixelColorVals[1]/255)**gammaval) # Negate green pixel
      bluePixel   = int(255*(pixelColorVals[2]/255)**gammaval) # Negate blue pixel
      # Modify the image with the inverted pixel values
      new_image.putpixel((i,j),(int(redPixel), int(greenPixel), int(bluePixel)))
  displayimage(new_image)
  stoping_to_draw()
  gamma_sli_label.configure(text=f"{round(gammaval,2)}")

def save_filter():
  global img
  img=new_image
  displayimage(img)
  stoping_to_draw()
  bri_sli.set(0)
  cat_sli.set(0)
  sat_sli.set(0)
  gamma_sli.set(1)
  blur_sli.set(0)
  bri_sli_label.configure(text="0")
  cat_sli_label.configure(text="0")
  sat_sli_label.configure(text="0")
  blur_sli_label.configure(text="0")
  gamma_sli_label.configure(text="1")

# opening images initiation
########
def initiate_opening():
  global icon,image_id
  icon=Image.open("logo/workarea_image_icon.png")
  icon=ImageTk.PhotoImage(icon)
  workarea.create_image(0,0,image=icon,anchor="nw")
  image_id=workarea.create_image(0,0, anchor="nw")
# getting the previous image after crop,sticker,etc
# 
def pre_img():
  global img
  width,height=img.size
  new = Image.new("RGB", (width, height), "white")
  for i in range(0,img.width-1):
    for j in range(0,img.height-1):
      if i > width or j > height:
        break
      pixel=img.getpixel((i,j))
      red=pixel[0]
      green=pixel[1]
      blue=pixel[2]
      new.putpixel((i,j),(red,green,blue))
  return new
#drawing shapes
def background_color():
  global background_color_shape
  _,background_color_shape=colorchooser.askcolor(title="Choose Color")
  colorchooser_background_l.configure(bg=background_color_shape,fg=background_color_shape)
#rectangle
def rectangle():
  global background_color_shape
  background_color_shape=None
  stoping_to_draw()
  workarea.bind("<Button-1>",get_x_and_y)
  workarea.bind("<ButtonRelease-1>",release_r)
def release_r(event):
  global new_image
  new_image=pre_img()
  x1 = ImageDraw.Draw(new_image)
  x1.rectangle([(lasx,lasy),(event.x,event.y)],fill=background_color_shape,outline=current_color,width=int(shape_width.get()))
  displayimage(new_image)
#circle
def circle():
  global background_color_shape
  background_color_shape=None
  stoping_to_draw()
  workarea.bind("<Button-1>",get_x_and_y)
  workarea.bind("<ButtonRelease-1>",release_c)
def release_c(event):
  global new_image
  new_image=pre_img()
  x1 = ImageDraw.Draw(new_image)
  x1.ellipse([(lasx,lasy),(event.x,event.y)],fill=background_color_shape,outline=current_color,width=int(shape_width.get()))
  displayimage(new_image)
#arc 
def arc():
  global background_color_shape
  background_color_shape=None
  stoping_to_draw()
  workarea.bind("<Button-1>",get_x_and_y)
  workarea.bind("<ButtonRelease-1>",release_arc)
def release_arc(event):
  global new_image
  new_image=pre_img()
  x1 = ImageDraw.Draw(new_image)
  x1.pieslice([(lasx,lasy),(event.x,event.y)],start=0,end=int(arc_angle.get()),fill=background_color_shape,outline=current_color,width=int(shape_width.get()))
  displayimage(new_image)


#WRITING

def write_text():
  stoping_to_draw()
  workarea.bind("<Button-1>",write_)
def write_(event):
  global new_image
  new_image=pre_img()
  x1 = ImageDraw.Draw(new_image)
  font = ImageFont.truetype(f"font/{fonts.get()}.ttf",int(shape_width.get()))
  x1.text((event.x, event.y), text_entry.get(), fill=current_color,font=font,stroke_width=int(bold_width.get()))
  displayimage(new_image)
  



# crop
def crop():
  global new_img
  stoping_to_draw()
  new_img=pre_img()
  workarea.bind("<Button-1>",get_x_and_y)
  workarea.bind("<ButtonRelease-1>",crop_)

def crop_(event):
  global img
  img=img.crop((lasx,lasy,event.x,event.y))
  w=workarea_set_widthentry
  h=workarea_set_heightentry
  img=img.resize((w,h))
  displayimage(img)

def reverse_crop():
  global img
  img=new_img
  displayimage(img)
#pasting image on image

def emoji_image():
  global ratio,emoji_
  stoping_to_draw()
  imgname_emoji =filedialog.askopenfilename (title="open")
  if imgname_emoji:
    emoji_ = Image.open(imgname_emoji).convert('RGBA')
    ratio=int(emoji_.width/emoji_.height)
  workarea.bind("<Button-1>",write_emoji)
  
def write_emoji(event):
  global new_image
  new_image=pre_img()  
  emoji = emoji_.resize((int(emoji_width.get()),int(emoji_width.get()/ratio)))
  mask_im = Image.new("L", emoji.size, 0)
  for i in range(emoji.size[0]):
    for j in range(emoji.size[1]):
        pixel=emoji.getpixel((i,j))
        if pixel[3]!=0:
          pixel=225
        else:
          pixel=0
        mask_im.putpixel((i,j),pixel)
  new_image.paste(emoji,(event.x,event.y),mask_im)
  displayimage(new_image)


# settings
def settings():
  global setting,setting_checkbox_button,workarea_set_widthvalue,workarea_set_heightvalue
  setting=customtkinter.CTk()
  setting.geometry("450x450")
  setting.title("Settings")
  setting.config(padx=10,pady=10)
  set_frame_1=customtkinter.CTkFrame(setting)
  set_frame_1.place(x=0,y=0,relwidth=1,relheight=1)
  customtkinter.CTkLabel(set_frame_1,text="Image display",font=("Times New Roman",15,"bold")).grid(row=0,column=0)
  customtkinter.CTkLabel(set_frame_1,text="Width",font=("Times New Roman",15,"bold")).grid(row=1,column=0)
  customtkinter.CTkLabel(set_frame_1,text="height",font=("Times New Roman",15,"bold")).grid(row=2,column=0)
  def workarea_set_slider(var):
    workarea_set_heightvalue_label.configure(text=f"{round(workarea_set_heightvalue.get(),1)}")
    workarea_set_widthvalue_label.configure(text=f"{round(workarea_set_widthvalue.get(),1)}")

  workarea_set_widthvalue=customtkinter.CTkSlider(set_frame_1,from_=100, to=900, command=workarea_set_slider)
  workarea_set_widthvalue.grid(row=1, column=1)
  workarea_set_widthvalue.set(574)
  workarea_set_heightvalue=customtkinter.CTkSlider(set_frame_1,from_=100, to=900, command=workarea_set_slider)
  workarea_set_heightvalue.grid(row=2, column=1)
  workarea_set_heightvalue.set(429)
  workarea_set_widthvalue_label=customtkinter.CTkLabel(set_frame_1,text=workarea_set_widthvalue.get())
  workarea_set_widthvalue_label.grid(row=1,column=2)
  workarea_set_heightvalue_label=customtkinter.CTkLabel(set_frame_1,text=workarea_set_heightvalue.get())
  workarea_set_heightvalue_label.grid(row=2,column=2)

  
  customtkinter.CTkLabel(set_frame_1,text="Include pencil drawn content",wraplength=100,font=("Times New Roman",15,"bold")).grid(row=3,column=0)
  setting_checkbox_button = customtkinter.CTkCheckBox(master=set_frame_1,text="check it")
  setting_checkbox_button.grid(row=3, column=1, pady=10, padx=20)
  customtkinter.CTkButton(text="Apply",master=set_frame_1, command=apply_workarea_window).grid(row=4,column=0,padx=20, pady=10)
  customtkinter.CTkButton(text="close",master=set_frame_1, command=close_setting_tab).grid(row=4,column=1,padx=20, pady=10)
  
  setting.mainloop()
def apply_workarea_window():
  global workarea_set_heightentry, workarea_set_widthentry,checkbox_button_new
  workarea_set_widthentry=int(workarea_set_widthvalue.get())
  workarea_set_heightentry=int(workarea_set_heightvalue.get())
  checkbox_button_new=setting_checkbox_button.get()
  setting.destroy()
  
def close_setting_tab():
  setting.destroy()


# shape width,draw width, bold width updater 
def shape_width_slider(var):
  text_=round(shape_width.get(),1)
  shape_width_label.configure(text=text_)
  text_=round(bold_width.get(),1)
  bold_width_label.configure(text=f"bold-{text_}")
  text_=round(brush_slider.get(),1)
  brush_slider_label.configure(text=text_)
  text_=round(emoji_width.get(),1)
  emoji_width_label.configure(text=text_)
#arc angle slider
def arc_angle_slider(var):
  angle_value=f"{round(arc_angle.get(),1)} °"
  arc_angle_label.configure(text=angle_value)
# saving the image
#########
def save():
  global img
  global imgname
  ext=re.findall(r"\.+\w+",imgname)
  if checkbox_button_new==0:
    if widthvalue.get()==0 and heightvalue.get()==0:
      dimension=Image.open(imgname)
      img=img.resize((dimension.width,dimension.height))
    else:
      resize_()
  else:
    if widthvalue.get()==0 and heightvalue.get()==0:
      dimension=Image.open(imgname)
      x=workarea.winfo_rootx()
      y=workarea.winfo_rooty()
      img=ImageGrab.grab(bbox=(x,y,x+workarea_set_widthentry,y+workarea_set_heightentry))
      img=img.resize((dimension.width,dimension.height))
    else:
      x=workarea.winfo_rootx()
      y=workarea.winfo_rooty()
      if widthvalue.get()>=workarea_set_widthentry:
        width=workarea_set_widthentry
      else:
        width=widthvalue.get()
      if heightvalue.get()>=workarea_set_heightentry:
        height=workarea_set_heightentry
      else:
        height=heightvalue.get()
      img=img.resize((widthvalue.get(),heightvalue.get()))#since after resizing more than workarea dimension resize was not working
      img=ImageGrab.grab(bbox=(x,y,x+width,y+height))

  imgname =filedialog.asksaveasfilename (title="save",defaultextension=ext[0])
  if imgname:
    img.save(imgname)
  stoping_to_draw()



# closing
def confirm():
  ans=tsmg.askyesno("Save and exit","Want to Exit! \n Did you save your work?")
  if ans:
    root_i.destroy()
  else:
    ans=tsmg.askyesno("Save and exit","Want to save your work?")
    if ans:
      save()
      root_i.destroy() 
    else:
      root_i.destroy()


# configure window

#########
# Nirmit Pratap Singh
root_i=customtkinter.CTk()
root_i.title("ediTIT")
Width= root_i.winfo_screenwidth()#
Height= root_i.winfo_screenheight()# both doe
root_i.geometry("%dx%d" % (Width, Height))
root_i.config(padx=10,pady=10)
top_logo=tkinter.PhotoImage(file="logo/anupam_chitra_editor.png")
root_i.iconphoto(False,top_logo)

# making the frames and tab view
top_frame = tkinter.Frame(root_i,bg="#333438")
top_frame.place(x=0,y=0,relwidth=1,relheight=0.1)

left_frame = customtkinter.CTkScrollableFrame(root_i)
left_frame.place(relx=0,rely=0.12,relwidth=0.2,relheight=0.88)

mid_frame = tkinter.Frame(root_i,bg="#333438")
mid_frame.place(relx=0.22,rely=0.12,relwidth=0.45,relheight=0.88)

right_tabs = customtkinter.CTkTabview(root_i)
right_tabs.place(relx=0.69,rely=0.12,relwidth=0.3,relheight=0.88)

right_tabs.add("Home")
right_tabs.add("Edit")
right_tabs.add("Insert")
right_tabs.add("Advance")

# top menu buttons
open_button = customtkinter.CTkButton(text="Import",master=top_frame, command=openimage)
open_button.grid(row=0, column=0, padx=20, pady=10)

save_button = customtkinter.CTkButton(text="Export",master=top_frame, command=save)
save_button.grid(row=0, column=1, padx=20, pady=10)

help_button = customtkinter.CTkButton(text="Help",master=top_frame, command=help)
help_button.grid(row=0, column=2, padx=20, pady=10)

about_button = customtkinter.CTkButton(text="About",master=top_frame, command=about)
about_button.grid(row=0, column=3, padx=20, pady=10)

about_button = customtkinter.CTkButton(text="Setting",master=top_frame, command=settings)
about_button.grid(row=0, column=4, padx=20, pady=10)

workarea_set_widthentry=574
workarea_set_heightentry=429
checkbox_button_new=0

# desiging the mid frame
work_area=tkinter.Frame(master=mid_frame, bg="#414041")
work_area.place(x=15,y=10,relheight=0.83,relwidth=0.95)

work_area_button_frame=tkinter.Frame(master=mid_frame, bg="#414041",padx=20)
work_area_button_frame.place(x=15,rely=0.875,relheight=0.1,relwidth=0.95)

reset_button = customtkinter.CTkButton(text="Reset",master=work_area_button_frame, command=reset_)
reset_button.grid(row=0, column=0, padx=20, pady=10)


# how opening content will look when open in workarea
workarea=tkinter.Canvas(work_area,bg="grey")
workarea.place(x=0,y=0,relheight=1,relwidth=1)
initiate_opening()

#
#
#home tab 
#
#
rotate=customtkinter.CTkButton(right_tabs.tab("Home"),command=rotate_,text="Rotate")
rotate.grid(row=0,column=0)
customtkinter.CTkLabel(right_tabs.tab("Home"),text=" ↺ ",font=("Times New Roman",30,"bold")).grid(row=0,column=1)

flip_h=customtkinter.CTkButton(right_tabs.tab("Home"),command=flip_lr,text="Flip Horizontal")
flip_h.grid(row=1,column=0)
customtkinter.CTkLabel(right_tabs.tab("Home"),text=" ↔ ",font=("Times New Roman",30,"bold")).grid(row=1,column=1)

flip_v=customtkinter.CTkButton(right_tabs.tab("Home"),command=flip_tb,text="Flip Verticle")
flip_v.grid(row=2,column=0)
customtkinter.CTkLabel(right_tabs.tab("Home"),text=" ↕ ",font=("Times New Roman",30,"bold")).grid(row=2,column=1)

customtkinter.CTkLabel(right_tabs.tab("Home"),text="Size-",font=("Times New Roman",30,"bold")).grid(row=3,column=0)

size_detail=customtkinter.CTkLabel(right_tabs.tab("Home"),text="----x----",font=("Times New Roman",25,"bold"))
size_detail.grid(row=4,column=1)

resize_b=customtkinter.CTkButton(right_tabs.tab("Home"),command=resize_,text="Resize")
resize_b.grid(row=5,column=0)

customtkinter.CTkLabel(right_tabs.tab("Home"),text="Width-",font=("Times New Roman",30,"bold")).grid(row=6,column=0)

customtkinter.CTkLabel(right_tabs.tab("Home"),text="Height-",font=("Times New Roman",30,"bold")).grid(row=7,column=0)

widthvalue=tkinter.IntVar()
heightvalue=tkinter.IntVar()

widthentry=customtkinter.CTkEntry(right_tabs.tab("Home"),textvariable=widthvalue)
heightentry=customtkinter.CTkEntry(right_tabs.tab("Home"),textvariable=heightvalue)

widthentry.grid(row=6,column=1)
heightentry.grid(row=7,column=1)

current_color="#000000"
brush_width=1

draw_b=customtkinter.CTkButton(right_tabs.tab("Home"),command=draw,text="Draw")
draw_b.grid(row=8,column=0)
customtkinter.CTkLabel(right_tabs.tab("Home"),text=" ✐ ",font=("Times New Roman",30,"bold")).grid(row=8,column=1)

clear_b=customtkinter.CTkButton(right_tabs.tab("Home"),command=clear,text="Clear")
clear_b.grid(row=9,column=0)
customtkinter.CTkLabel(right_tabs.tab("Home"),text=" ✗ ",font=("Times New Roman",30,"bold")).grid(row=9,column=1)

customtkinter.CTkLabel(right_tabs.tab("Home"),text="Brush Width",font=("Times New Roman",30,"bold")).grid(row=10,column=0)

brush_slider= customtkinter.CTkSlider(right_tabs.tab("Home"),from_=brush_width, to=15, command=shape_width_slider)
brush_slider.set(brush_width)
brush_slider.grid(row=11, column=0)
brush_slider_label=customtkinter.CTkLabel(right_tabs.tab("Home"),text=brush_slider.get())
brush_slider_label.grid(row=11,column=1)

colorchooser_b=customtkinter.CTkButton(right_tabs.tab("Home"),command=choose_color,text="Color")
colorchooser_b.grid(row=12,column=0)
colorchooser_b_l_d=tkinter.Label(right_tabs.tab("Home"),text="--",bg=current_color)
colorchooser_b_l_d.grid(row=12,column=1)

#
#
#
#filters
#
#
#
  
filter_image=["filter images/emboss.jpg","filter images/contour.jpg","filter images/gray.jpg","filter images/sketch.jpg","filter images/negative.jpg","filter images/sepai.jpg","filter images/pointilize.jpg","filter images/cool.jpg","filter images/warm.jpg","filter images/fedges.jpg","filter images/detail.jpg"]

#way to add images in ctk button
photo_filter=customtkinter.CTkImage(light_image=Image.open(filter_image[0]),dark_image=Image.open(filter_image[0]),size=(180,150))
customtkinter.CTkButton(left_frame,image=photo_filter,command=emboss,text="").grid(row=0,column=0,padx=30,pady=(10,20))

photo_filter=customtkinter.CTkImage(light_image=Image.open(filter_image[1]),dark_image=Image.open(filter_image[1]),size=(180,150))
customtkinter.CTkButton(left_frame,image=photo_filter,command=contour,text="").grid(row=1,column=0,padx=30,pady=(10,20))

photo_filter=customtkinter.CTkImage(light_image=Image.open(filter_image[2]),dark_image=Image.open(filter_image[2]),size=(180,150))
customtkinter.CTkButton(left_frame,image=photo_filter,command=gray,text="").grid(row=2,column=0,padx=30,pady=(10,20))

photo_filter=customtkinter.CTkImage(light_image=Image.open(filter_image[3]),dark_image=Image.open(filter_image[3]),size=(180,150))
customtkinter.CTkButton(left_frame,image=photo_filter,command=sketch,text="").grid(row=3,column=0,padx=30,pady=(10,20))

photo_filter=customtkinter.CTkImage(light_image=Image.open(filter_image[4]),dark_image=Image.open(filter_image[4]),size=(180,150))
customtkinter.CTkButton(left_frame,image=photo_filter,command=negative,text="").grid(row=4,column=0,padx=30,pady=(10,20))

photo_filter=customtkinter.CTkImage(light_image=Image.open(filter_image[5]),dark_image=Image.open(filter_image[5]),size=(180,150))
customtkinter.CTkButton(left_frame,image=photo_filter,command=sepai,text="").grid(row=5,column=0,padx=30,pady=(10,20))

photo_filter=customtkinter.CTkImage(light_image=Image.open(filter_image[6]),dark_image=Image.open(filter_image[6]),size=(180,150))
customtkinter.CTkButton(left_frame,image=photo_filter,command=pointilize,text="").grid(row=6,column=0,padx=30,pady=(10,20))

photo_filter=customtkinter.CTkImage(light_image=Image.open(filter_image[7]),dark_image=Image.open(filter_image[7]),size=(180,150))
customtkinter.CTkButton(left_frame,image=photo_filter,command=cool,text="").grid(row=7,column=0,padx=30,pady=(10,20))

photo_filter=customtkinter.CTkImage(light_image=Image.open(filter_image[8]),dark_image=Image.open(filter_image[8]),size=(180,150))
customtkinter.CTkButton(left_frame,image=photo_filter,command=warm,text="").grid(row=8,column=0,padx=30,pady=(10,20))

photo_filter=customtkinter.CTkImage(light_image=Image.open(filter_image[9]),dark_image=Image.open(filter_image[9]),size=(180,150))
customtkinter.CTkButton(left_frame,image=photo_filter,command=fedges,text="").grid(row=9,column=0,padx=30,pady=(10,20))

photo_filter=customtkinter.CTkImage(light_image=Image.open(filter_image[10]),dark_image=Image.open(filter_image[10]),size=(180,150))
customtkinter.CTkButton(left_frame,image=photo_filter,command=detail_filter,text="").grid(row=10,column=0,padx=30,pady=(10,20))
#
#
#
#
#Insert tab
#
#
#
customtkinter.CTkButton(right_tabs.tab("Insert"),command=rectangle,text="rectangle").grid(row=0,column=0)
customtkinter.CTkLabel(right_tabs.tab("Insert"),text=" ▭ ",font=("Times New Roman",30,"bold")).grid(row=0,column=1)

customtkinter.CTkButton(right_tabs.tab("Insert"),command=circle,text="circle").grid(row=1,column=0)
customtkinter.CTkLabel(right_tabs.tab("Insert"),text=" o ",font=("Times New Roman",30,"bold")).grid(row=1,column=1)
customtkinter.CTkButton(right_tabs.tab("Insert"),command=save_filter,text="Save-shape").grid(row=1,column=2)

customtkinter.CTkButton(right_tabs.tab("Insert"),command=arc,text="arc").grid(row=2,column=0)
customtkinter.CTkLabel(right_tabs.tab("Insert"),text=" ⌒ ",font=("Times New Roman",30,"bold")).grid(row=2,column=1)

customtkinter.CTkLabel(right_tabs.tab("Insert"),text="Arc Angle",font=("Times New Roman",30,"bold")).grid(row=3,column=0)
arc_angle_val=90
arc_angle= customtkinter.CTkSlider(right_tabs.tab("Insert"),from_=0, to=360,command=arc_angle_slider)
arc_angle.set(arc_angle_val)
arc_angle.grid(row=4, column=0)
arc_angle_label=customtkinter.CTkLabel(right_tabs.tab("Insert"),text=f"{arc_angle.get()} °")
arc_angle_label.grid(row=4,column=1)

customtkinter.CTkLabel(right_tabs.tab("Insert"),text="Width",font=("Times New Roman",30,"bold")).grid(row=5,column=0)
shape_width_val=1
shape_width= customtkinter.CTkSlider(right_tabs.tab("Insert"),from_=brush_width, to=50,command=shape_width_slider)
shape_width.set(shape_width_val)
shape_width.grid(row=6, column=0)
shape_width_label=customtkinter.CTkLabel(right_tabs.tab("Insert"),text=shape_width.get())
shape_width_label.grid(row=6,column=1)

colorchooser_b=customtkinter.CTkButton(right_tabs.tab("Insert"),command=choose_color,text="Color")
colorchooser_b.grid(row=7,column=0)
colorchooser_b_l=tkinter.Label(right_tabs.tab("Insert"),text="--",bg=current_color)
colorchooser_b_l.grid(row=7,column=1)

customtkinter.CTkLabel(right_tabs.tab("Insert"),text="Fill color",font=("Times New Roman",30,"bold")).grid(row=8,column=0)
background_color_shape=""
customtkinter.CTkButton(right_tabs.tab("Insert"),command=background_color,text="FillColor").grid(row=9,column=0)
colorchooser_background_l=tkinter.Label(right_tabs.tab("Insert"),text="--",bg=current_color)
colorchooser_background_l.grid(row=9,column=1)

text_entry = customtkinter.CTkEntry(right_tabs.tab("Insert"), placeholder_text="Write text here")
text_entry.grid(row=10, column=0, columnspan=2, padx=(20, 0), pady=(20, 20),sticky="nsew")

customtkinter.CTkButton(right_tabs.tab("Insert"),command=write_text,text="Write").grid(row=10,column=2)

fonts = customtkinter.CTkOptionMenu(right_tabs.tab("Insert"), dynamic_resizing=False,values=["Arial","Times_New_Roman","AgreementSignature-qZX6x","ArianaVioleta-dz2K","Freedom-10eM","GreatVibes-Wmr4","HeyOctober-Yz37y","Mefikademo-owEAq","MorganChalk-L3aJy","Pixellettersfull-BnJ5","SongstarFree-qLg1","SwanseaBold-D0ox","SwanseaBoldItalic-p3Dv","WinterSong-owRGB"])
fonts.grid(row=11, column=0)

customtkinter.CTkButton(right_tabs.tab("Insert"),command=save_filter,text="Save Text").grid(row=11,column=2)

bold_width= customtkinter.CTkSlider(right_tabs.tab("Insert"),from_=brush_width, to=10,command=shape_width_slider)
bold_width.set(0)
bold_width.grid(row=12, column=0)
bold_width_label=customtkinter.CTkLabel(right_tabs.tab("Insert"),text=f"bold-{bold_width.get()}")
bold_width_label.grid(row=12,column=1)
# 
# 
#Edit tab 
# 
# 
#

customtkinter.CTkButton(right_tabs.tab("Edit"),command=crop,text="Crop Image").grid(row=0,column=0)
customtkinter.CTkLabel(right_tabs.tab("Edit"),text="⌌⌍",font=("Times New Roman",30,"bold")).grid(row=0,column=1)
customtkinter.CTkButton(right_tabs.tab("Edit"),command=reverse_crop,text="No crop").grid(row=0,column=2)

customtkinter.CTkLabel(right_tabs.tab("Edit"),text="Brightness",font=("Times New Roman",30,"bold")).grid(row=1,column=0)
bri_sli= customtkinter.CTkSlider(right_tabs.tab("Edit"),from_=-80, to=80,command=bright)
bri_sli.set(0)
bri_sli.grid(row=2, column=0)
bri_sli_label=customtkinter.CTkLabel(right_tabs.tab("Edit"),text=f"{bri_sli.get()}")
bri_sli_label.grid(row=2,column=1)

customtkinter.CTkLabel(right_tabs.tab("Edit"),text="Saturation",font=("Times New Roman",30,"bold")).grid(row=3,column=0)
sat_sli= customtkinter.CTkSlider(right_tabs.tab("Edit"),from_=-80, to=80,command=saturation)
sat_sli.set(0)
sat_sli.grid(row=4, column=0)
sat_sli_label=customtkinter.CTkLabel(right_tabs.tab("Edit"),text=f"{sat_sli.get()}")
sat_sli_label.grid(row=4,column=1)

customtkinter.CTkLabel(right_tabs.tab("Edit"),text="Contrast",font=("Times New Roman",30,"bold")).grid(row=5,column=0)
cat_sli= customtkinter.CTkSlider(right_tabs.tab("Edit"),from_=-100, to=100,command=contrast)
cat_sli.set(0)
cat_sli.grid(row=6, column=0)
cat_sli_label=customtkinter.CTkLabel(right_tabs.tab("Edit"),text=f"{cat_sli.get()}")
cat_sli_label.grid(row=6,column=1)

customtkinter.CTkLabel(right_tabs.tab("Edit"),text="Blur",font=("Times New Roman",30,"bold")).grid(row=7,column=0)
blur_sli= customtkinter.CTkSlider(right_tabs.tab("Edit"),from_=0, to=100,command=blur_)
blur_sli.set(0)
blur_sli.grid(row=8, column=0)
blur_sli_label=customtkinter.CTkLabel(right_tabs.tab("Edit"),text=f"{blur_sli.get()}")
blur_sli_label.grid(row=8,column=1)

customtkinter.CTkLabel(right_tabs.tab("Edit"),text="Gamma",font=("Times New Roman",30,"bold")).grid(row=9,column=0)
gamma_sli= customtkinter.CTkSlider(right_tabs.tab("Edit"),from_=0, to=2,command=gamma)
gamma_sli.set(1)
gamma_sli.grid(row=10, column=0)
gamma_sli_label=customtkinter.CTkLabel(right_tabs.tab("Edit"),text=f"{gamma_sli.get()}")
gamma_sli_label.grid(row=10,column=1)

customtkinter.CTkButton(right_tabs.tab("Edit"),command=save_filter,text="Save Filter").grid(row=11,column=0)
#
#
#
#

customtkinter.CTkButton(right_tabs.tab("Advance"),command=emoji_image,text="Image").grid(row=0,column=0)
customtkinter.CTkLabel(right_tabs.tab("Advance"),text=" ☺ ",font=("Times New Roman",30,"bold")).grid(row=0,column=1)
customtkinter.CTkButton(right_tabs.tab("Advance"),command=save_filter,text="Save image").grid(row=0,column=2)

customtkinter.CTkLabel(right_tabs.tab("Advance"),text="Image size",font=("Times New Roman",30,"bold")).grid(row=1,column=0)
emoji_width= customtkinter.CTkSlider(right_tabs.tab("Advance"),from_=50, to=600,command=shape_width_slider)
emoji_width.set(50)
emoji_width.grid(row=2, column=0)
emoji_width_label=customtkinter.CTkLabel(right_tabs.tab("Advance"),text=f"{emoji_width.get()}")
emoji_width_label.grid(row=2,column=1)

#
#
#
#
#
root_i.protocol("WM_DELETE_WINDOW",confirm)
root_i.mainloop()