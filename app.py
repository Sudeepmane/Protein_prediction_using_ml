from flask import Flask, request, render_template
from pipeline.predict_pipline import PredictPipeline,CustomData

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Collect input data from form
            data = CustomData(
                F1 = float(request.form.get("F1")),
                F2 = float(request.form.get("F2")),
                F3 = float(request.form.get("F3")),
                F4 = float(request.form.get("F4")),
                F5 = float(request.form.get("F5")),
                F6 = float(request.form.get("F6")),
                F7 = float(request.form.get("F7")),
                F8 = float(request.form.get("F8")),
                F9 = float(request.form.get("F9"))
            )

            # Convert into DataFrame
            final_new_data = data.get_data_as_data_frame()

            # Prediction
            predict_pipeline = PredictPipeline()
            pred = predict_pipeline.predict(final_new_data)

            return render_template("index.html", prediction_text=f"Predicted RMSD: {pred[0]}")

        except Exception as e:
            return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
