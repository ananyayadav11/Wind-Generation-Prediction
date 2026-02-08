from flask import Flask, render_template, request
import matplotlib
matplotlib.use('Agg')  # use Agg backend for Flask
import matplotlib.pyplot as plt
import pandas as pd
import os

# Import model functions
from model import model, create_pd

app = Flask(__name__)

# Features used by the model
features = ['hour', 'minute', 'day', 'month', 'year', 'dayofweek', 'dayofyear']

@app.route('/', methods=['GET', 'POST'])
def index():
    show_chart = False
    
    if request.method == 'POST':
        # Get form data
        from_date = request.form.get('fd')
        to_date = request.form.get('td')
        
        # Create DataFrame for predictions
        df = create_pd(from_date, to_date)
        fut = model.predict(df[features])
        future = pd.DataFrame(data={'Predictions': fut}, index=df.index)
        
        # Plot predictions
        plt.figure(figsize=(15, 5))
        plt.plot(future.index, future['Predictions'], linewidth=2, color='#4facfe')
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Energy Prediction (kW)', fontsize=12)
        plt.title('Wind Energy Generation Prediction', fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        # Save chart to static folder
        output_path = os.path.join(app.root_path, 'static', 'output.png')
        plt.savefig(output_path, dpi=100, bbox_inches='tight')
        plt.close()
        
        show_chart = True
    
    return render_template('index.html', show_chart=show_chart)

if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True)

