import math
from PIL import Image, ImageDraw, ImageFilter

# Create high-res canvas for supersampling (1024x1024 -> 256x256)
S = 1024
img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

def draw_star(center_x, center_y, size, color):
    # Draw an 8-point asterisk star
    for angle in [0, 45, 90, 135]:
        rad = math.radians(angle)
        dx = math.cos(rad) * size
        dy = math.sin(rad) * size
        draw.line([center_x - dx, center_y - dy, center_x + dx, center_y + dy], fill=color, width=int(size * 0.28))
    # Core circle
    r = size * 0.35
    draw.ellipse([center_x - r, center_y - r, center_x + r, center_y + r], fill=color)

# Colors
C_CYAN = (56, 189, 248, 255)       # #38bdf8
C_BLUE = (37, 99, 235, 255)        # #2563eb
C_PURPLE = (147, 51, 234, 255)     # #9333ea
C_GOLD = (251, 191, 36, 255)       # #fbbf24
C_LIGHT_GOLD = (254, 240, 138, 255)
C_DARK_BG = (15, 23, 42, 230)      # Translucent dark slate
C_WHITE = (255, 255, 255, 255)

# 1. House Body (Walls)
body_left = 220
body_right = 804
body_top = 460
body_bottom = 830

# Wall background (rounded rectangle)
draw.rounded_rectangle([body_left, body_top, body_right, body_bottom], radius=32, fill=(15, 23, 42, 210), outline=(56, 189, 248, 255), width=18)

# 2. Roof: Triangle with overhanging eaves
roof_peak = (512, 160)
roof_left = (150, 480)
roof_right = (874, 480)

# Roof fill
draw.polygon([roof_peak, (roof_left[0] + 50, roof_left[1]), (roof_right[0] - 50, roof_right[1])], fill=(30, 41, 59, 230))

# Roof outer thick frame
draw.line([roof_left, roof_peak, roof_right], fill=(56, 189, 248, 255), width=28, joint="curve")
# Inner roof contour (gradient feel)
draw.line([(roof_left[0] + 30, roof_left[1] - 10), (roof_peak[0], roof_peak[1] + 35), (roof_right[0] - 30, roof_right[1] - 10)], fill=(99, 102, 241, 255), width=12)

# Eaves caps
draw.ellipse([roof_left[0]-14, roof_left[1]-14, roof_left[0]+14, roof_left[1]+14], fill=(56, 189, 248, 255))
draw.ellipse([roof_right[0]-14, roof_right[1]-14, roof_right[0]+14, roof_right[1]+14], fill=(56, 189, 248, 255))

# 3. Windows (Left & Right)
w_size = 90
w_y = 530

# Left window
lw_x = 310
draw.rounded_rectangle([lw_x - w_size, w_y - w_size, lw_x + w_size, w_y + w_size], radius=16, fill=(251, 191, 36, 40), outline=C_GOLD, width=12)
# Window mullions
draw.line([lw_x, w_y - w_size + 4, lw_x, w_y + w_size - 4], fill=C_GOLD, width=8)
draw.line([lw_x - w_size + 4, w_y, lw_x + w_size - 4, w_y], fill=C_GOLD, width=8)

# Right window
rw_x = 714
draw.rounded_rectangle([rw_x - w_size, w_y - w_size, rw_x + w_size, w_y + w_size], radius=16, fill=(251, 191, 36, 40), outline=C_GOLD, width=12)
# Window mullions
draw.line([rw_x, w_y - w_size + 4, rw_x, w_y + w_size - 4], fill=C_GOLD, width=8)
draw.line([rw_x - w_size + 4, w_y, rw_x + w_size - 4, w_y], fill=C_GOLD, width=8)

# 4. Center Doorway
door_w = 90
door_top = 610
door_bottom = 830
draw.rounded_rectangle([512 - door_w, door_top, 512 + door_w, door_bottom], radius=24, fill=(30, 41, 59, 255), outline=(56, 189, 248, 255), width=14)
# Door inner panel
draw.rounded_rectangle([512 - door_w + 18, door_top + 20, 512 + door_w - 18, door_bottom], radius=14, fill=(15, 23, 42, 255), outline=(99, 102, 241, 180), width=6)
# Door knob (golden star/dot)
draw.ellipse([512 + 35, 725, 512 + 55, 745], fill=C_GOLD)

# 5. Foundation Base
draw.line([(180, 846), (844, 846)], fill=(56, 189, 248, 255), width=20)
draw.line([(240, 874), (784, 874)], fill=(99, 102, 241, 255), width=12)

# 6. Asterisk Stars (Signature feature of C house!)
# Big Spire Star at Roof Peak
draw_star(512, 140, 45, C_GOLD)

# Small celestial asterisk sparks
draw_star(280, 260, 24, C_LIGHT_GOLD)
draw_star(744, 260, 24, C_LIGHT_GOLD)
draw_star(190, 360, 16, C_CYAN)
draw_star(834, 360, 16, C_CYAN)

# Attic vent star
draw_star(512, 380, 28, C_CYAN)

# Resize down to 256x256 with high quality Lanczos resampling for smooth edges
final_img = img.resize((256, 256), Image.Resampling.LANCZOS)
final_img.save("assets/house_logo.png", "PNG")
print("Saved assets/house_logo.png successfully!")
