print("Script started successfully!")

import os
import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO
print("Libraries imported successfully!")

# Load YOLOv8 model
model = YOLO("yolov8n.pt")
print("YOLOv8 model loaded successfully!")

# Image path
image_path = r"C:\Users\Asus\Downloads\bernice mini project\traffic.jpg"

# Check if image exists
if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image not found at: {image_path}")

print("Processing image:", image_path)

# Perform detection
results = model.predict(source=image_path, conf=0.4, verbose=False)

# Count vehicles
vehicle_classes = ["car", "motorcycle", "bus", "truck"]
vehicle_count = {v: 0 for v in vehicle_classes}

for result in results:
    if result.boxes is not None:
        for box in result.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            if label in vehicle_classes:
                vehicle_count[label] += 1

print("\nVehicle Count:")
for v, c in vehicle_count.items():
    print(f"{v.capitalize()}: {c}")

# Save annotated image
annotated_image = results[0].plot()
cv2.imwrite("detected_vehicles.jpg", annotated_image)
print("Detected image saved as detected_vehicles.jpg")


# Display annotated image
annotated_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
plt.imshow(annotated_rgb)
plt.title("Detected Vehicles")
plt.axis("off")
plt.show(block=False)
plt.pause(3)
plt.close()

# Plot graph
plt.bar(vehicle_count.keys(), vehicle_count.values())
plt.title("Vehicle Count Distribution")
plt.xlabel("Vehicle Type")
plt.ylabel("Count")
plt.savefig("vehicle_count_graph.png")
plt.show(block=False)
plt.pause(3)
plt.close()


print("Graph saved as vehicle_count_graph.png")
print("Program executed successfully!")

print("🚨 SIGNAL CODE STARTING 🚨")


print("Script started successfully!")

import os
import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO
import tkinter as tk

print("Libraries imported successfully!")

# ================= VEHICLE DETECTION =================

# Load YOLOv8 model
model = YOLO("yolov8n.pt")
print("YOLOv8 model loaded successfully!")

# Image path (MAKE SURE THIS IS CORRECT)
image_path = r"C:\Users\Asus\Downloads\bernice mini project\traffic.jpg"

if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image not found at: {image_path}")

print("Processing image:", image_path)

# Perform detection
results = model.predict(source=image_path, conf=0.4, verbose=False)

# Count vehicles
vehicle_classes = ["car", "motorcycle", "bus", "truck"]
vehicle_count = {v: 0 for v in vehicle_classes}

for result in results:
    if result.boxes is not None:
        for box in result.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            if label in vehicle_classes:
                vehicle_count[label] += 1

print("\nVehicle Count:")
for v, c in vehicle_count.items():
    print(f"{v.capitalize()}: {c}")

# ================= IMAGE OUTPUT =================

annotated_image = results[0].plot()
cv2.imwrite("detected_vehicles.jpg", annotated_image)

annotated_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
plt.imshow(annotated_rgb)
plt.title("Detected Vehicles")
plt.axis("off")
plt.show(block=False)
plt.pause(3)
plt.close()

# ================= GRAPH OUTPUT =================

plt.bar(vehicle_count.keys(), vehicle_count.values())
plt.title("Vehicle Count Distribution")
plt.xlabel("Vehicle Type")
plt.ylabel("Count")
plt.savefig("vehicle_count_graph.png")
plt.show(block=False)
plt.pause(3)
plt.close()

# ================= SMART SIGNAL SYSTEM =================

print("\n--- SIGNAL SYSTEM STARTED ---")

total_vehicles = sum(vehicle_count.values())

# Density logic
if total_vehicles < 5:
    density = "LOW"
    green_time = 5000
elif total_vehicles < 15:
    density = "MEDIUM"
    green_time = 10000
else:
    density = "HIGH"
    green_time = 15000

print("Traffic Density:", density)
print("Green Time:", green_time//1000, "sec")

# ================= GUI =================

root = tk.Tk()
root.title("Smart Traffic Signal")
root.geometry("300x550")
root.configure(bg="black")

canvas = tk.Canvas(root, width=200, height=400, bg="black", highlightthickness=0)
canvas.pack(pady=20)

# Lights
red_light = canvas.create_oval(50, 50, 150, 150, fill="grey")
yellow_light = canvas.create_oval(50, 170, 150, 270, fill="grey")
green_light = canvas.create_oval(50, 290, 150, 390, fill="grey")

# Labels
density_label = tk.Label(root, text=f"Density: {density}", fg="white", bg="black", font=("Arial", 12))
density_label.pack()

time_label = tk.Label(root, text="", fg="white", bg="black", font=("Arial", 10))
time_label.pack()

# ================= COUNTDOWN SYSTEM =================

def countdown_phase(time_left, label_text, next_func):
    if time_left >= 0:
        time_label.config(text=f"{label_text}: {time_left//1000} sec")
        root.after(1000, countdown_phase, time_left - 1000, label_text, next_func)
    else:
        next_func()

# ================= SIGNAL FLOW =================

def red_phase():
    canvas.itemconfig(red_light, fill="red")
    canvas.itemconfig(yellow_light, fill="grey")
    canvas.itemconfig(green_light, fill="grey")
    countdown_phase(3000, "RED (STOP)", green_phase)

def green_phase():
    canvas.itemconfig(red_light, fill="grey")
    canvas.itemconfig(yellow_light, fill="grey")
    canvas.itemconfig(green_light, fill="green")
    countdown_phase(green_time, "GREEN (GO)", yellow_phase)

def yellow_phase():
    canvas.itemconfig(red_light, fill="grey")
    canvas.itemconfig(yellow_light, fill="yellow")
    canvas.itemconfig(green_light, fill="grey")
    countdown_phase(3000, "YELLOW (WAIT)", root.destroy)

# Start signal
red_phase()

root.mainloop()

print("Program executed successfully!")