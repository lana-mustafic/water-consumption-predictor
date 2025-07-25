import tkinter as tk
from tkinter import ttk, messagebox
import requests
import threading

class WaterConsumptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Household Water Consumption Predictor")
        self.root.geometry("450x400")

        # Main container
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Input Frame
        input_frame = ttk.LabelFrame(self.main_frame, text="Household Details", padding=10)
        input_frame.pack(fill="x", pady=5)

        # Input fields 
        ttk.Label(input_frame, text="Number of Occupants:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.occupants_entry = ttk.Entry(input_frame)
        self.occupants_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Average Temperature (°C):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.temp_entry = ttk.Entry(input_frame)
        self.temp_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Household Type:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.household_type = ttk.Combobox(input_frame, values=["Apartment", "House"])
        self.household_type.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Outdoor Activities:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.outdoor_activities = ttk.Combobox(input_frame, values=["Yes", "No"])
        self.outdoor_activities.grid(row=3, column=1, padx=5, pady=5)

        # Button Frame 
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=10)

        # Predict Button
        self.predict_btn = ttk.Button(button_frame, text="Predict", command=self.start_prediction_thread)
        self.predict_btn.grid(row=0, column=0, padx=5)

        # Clear Button
        self.clear_btn = ttk.Button(button_frame, text="Clear", command=self.clear)
        self.clear_btn.grid(row=0, column=1, padx=5)

        # Result Frame
        result_frame = ttk.LabelFrame(self.main_frame, text="Prediction Result", padding=10)
        result_frame.pack(fill="both", expand=True, pady=5)

        self.result_label = ttk.Label(result_frame, text="Enter details and click 'Predict'", font=('Arial', 10))
        self.result_label.pack()

        # Progress Bar 
        self.progress = ttk.Progressbar(result_frame, mode='indeterminate')
        self.progress.pack(fill='x', pady=5)
        self.progress.stop()

    def start_prediction_thread(self):
        """Start prediction in background thread"""
        self.predict_btn.config(state="disabled")
        self.result_label.config(text="Loading...")
        self.progress.start()
        threading.Thread(target=self.predict, daemon=True).start()

    def clear(self):
        """Reset all fields"""
        self.occupants_entry.delete(0, tk.END)
        self.temp_entry.delete(0, tk.END)
        self.household_type.set('')
        self.outdoor_activities.set('')
        self.result_label.config(text="Enter details and click 'Predict'")
        self.progress.stop()
        self.predict_btn.config(state="normal")

    def predict(self):
        try:
            data = {
                'Number_of_Occupants': int(self.occupants_entry.get()),
                'Average_Temperature': float(self.temp_entry.get()),
                'Household_Type': self.household_type.get(),
                'Outdoor_Activities': self.outdoor_activities.get()
            }

            if not all(data.values()):
                self.root.after(0, lambda: messagebox.showerror("Error", "Please fill all fields"))
                return

            response = requests.post('http://localhost:5000/predict', json=data)
            self.root.after(0, self.update_result, response)

        except ValueError:
            self.root.after(0, lambda: messagebox.showerror("Error", "Invalid number input"))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", str(e)))
        finally:
            self.root.after(0, lambda: [self.progress.stop(), self.predict_btn.config(state="normal")])

    def update_result(self, response):
        """Update UI with prediction result"""
        if response.status_code == 200:
            result = response.json()
            self.result_label.config(text=f"Predicted: {result['prediction']} liters")
        else:
            messagebox.showerror("Error", f"API Error: {response.text}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WaterConsumptionApp(root)
    root.mainloop()