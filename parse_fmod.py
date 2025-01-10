import xml.etree.ElementTree as ET
import json
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def select_input_directory():
    input_dir = filedialog.askdirectory()
    input_entry.delete(0, tk.END)
    input_entry.insert(0, input_dir)

def select_output_directory():
    output_dir = filedialog.askdirectory()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_dir)

def process_files():
    directory_path = input_entry.get()
    output_directory = output_entry.get()

    if not directory_path or not output_directory:
        messagebox.showerror("Error", "Please select both input and output directories.")
        return

    os.makedirs(output_directory, exist_ok=True)

    for filename in os.listdir(directory_path):
        if filename.endswith(".xml"):
            file_path = os.path.join(directory_path, filename)
            tree = ET.parse(file_path)
            root = tree.getroot()

            chart_data = {
                "keyType": 4,
                "bpmData": {
                    "bpmChanges": []
                },
                "difficulties": [
                    {
                        "difficultyName": "Hard",
                        "notes": []
                    }
                ]
            }

            event_name = ""
            for obj in root.findall("object"):
                if obj.get("class") == "Event":
                    event_name = obj.find("property[@name='name']/value").text
                    break

            for obj in root.findall("object"):
                if obj.get("class") == "Event":
                    for rel in obj.findall("relationship"):
                        if rel.get("name") == "mixerInput":
                            bpm_value = 120.0
                            chart_data["bpmData"]["bpmChanges"].append({
                                "startTimeSec": 0.0,
                                "bpm": bpm_value,
                                "beatsPerMeasure": 4
                            })

            for obj in root.findall("object"):
                if obj.get("class") == "Timeline":
                    for marker_rel in obj.findall("relationship[@name='markers']"):
                        for destination in marker_rel.findall("destination"):
                            marker_id = destination.text
                            for marker_obj in root.findall("object"):
                                if marker_obj.get("id") == marker_id and marker_obj.get("class") == "NamedMarker":
                                    marker_position = float(marker_obj.find("property[@name='position']/value").text)
                                    chart_data["difficulties"][0]["notes"].append({
                                        "timeSec": marker_position,
                                        "lane": 0,
                                        "noteType": "Normal",
                                        "isLong": False,
                                        "length": 0.0
                                    })

            output_file_name = f"{event_name}.json"
            output_file_path = os.path.join(output_directory, output_file_name)
            with open(output_file_path, 'w', encoding='utf-8') as json_file:
                json.dump(chart_data, json_file, ensure_ascii=False, indent=4)

            print(f"{output_file_path} 파일이 생성되었습니다.")

    messagebox.showinfo("Success", "All files processed successfully.")

# GUI 설정
root = tk.Tk()
root.title("XML to JSON Converter")

# 입력 경로
input_label = tk.Label(root, text="Select Input Directory:")
input_label.pack()
input_entry = tk.Entry(root, width=50)
input_entry.pack()
input_button = tk.Button(root, text="Browse", command=select_input_directory)
input_button.pack()

# 출력 경로
output_label = tk.Label(root, text="Select Output Directory:")
output_label.pack()
output_entry = tk.Entry(root, width=50)
output_entry.pack()
output_button = tk.Button(root, text="Browse", command=select_output_directory)
output_button.pack()

# 실행 버튼
process_button = tk.Button(root, text="Process Files", command=process_files)
process_button.pack()

# GUI 실행
root.mainloop()