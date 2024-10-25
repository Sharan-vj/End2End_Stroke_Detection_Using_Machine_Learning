# End2End Stroke Detection Using Machine Learning

### Project Description
<p align='justify'> This project focuses on building an end-to-end machine learning model to predict the risk of stroke based on various medical and demographic parameters. By analyzing factors such as age, gender, hypertension, heart disease history, average glucose levels, and body mass index (BMI), the model aims to assist healthcare professionals in early detection and preventive measures. The web-based application built around the model offers a quick and user-friendly interface for predictions, supporting individuals in taking timely action to mitigate risks. </p>

### Screenshot
<img width="800" height="400" align="center" src="/screenshots/sample_image.png">

### Technologies Used in This Project
* Python: Core programming language for model development and web integration
* Pandas: For data manipulation and analysis
* Scikit-learn: For building, training, and evaluating the machine learning model
* MLflow: For tracking experiments and optimizing the model performance
* Flask: To deploy the model as a web application
* Jupyter Notebook: For exploratory data analysis (EDA) and model development
* HTML/CSS: To design the web-based user interface
* Git/GitHub: For version control and project hosting
* Docker: For Containerizing the application
* GitHub Action: For managing all CICD workflows
* AWS: For deploying the ML application

### Installation and Setup

1. **Clone the Repository**:
    ```bash
    git clone End2End_Stroke_Detection_Using_Machine_Learning.git
    cd End2End_Stroke_Detection_Using_Machine_Learning
    ```

2. **Create a Virtual Environment**:
    ```bash
    conda create --name <env name> python=3.10 -y
    ```
3. **Activate the Virtual Enviroment**
    ```bash
    conda activate <env name>
    ```
4. **Install the Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Flask Application**:
    ```bash
    python app.py
    ```
    The application will be available at `http://127.0.0.1:8080/`.

6. **Note**:

    In Default, This project will track parameters and metrics in local mlflow tracking uri `http://127.0.0.1:5000/`. To view experiments run the below command from project directory

    ```bash
    mlflow ui
    ```
    and open `http://127.0.0.1:5000/` this url.


### DagsHub Integration (Optional)

1. Create .env file in project main directory and Store below environment variables with required values from dagshub.
    ```
    MLFLOW_TRACKING_URI = " "
    MLFLOW_TRACKING_USERNAME = " "
    MLFLOW_TRACKING_PASSWORD = " "
    ```

2. Change the tracking URI `http://127.0.0.1:5000` to `MLFLOW_TRACKING_URI` in `model_trainer.py` and `model_evaluation.py` found in src/components folder.

### Usage
* Input Health Data: Use the web interface to input parameters such as age, BMI, glucose level, etc.
* Get Prediction: The trained model will predict whether the patient is at risk of a stroke based on the provided inputs.

### Dataset
* The dataset used for this project contains information on patients demographic and health metrics along with labels indicating whether they have experienced a stroke. The dataset is stored in the data/ directory.

### Model
* The prediction model is built using Scikit-learn. After training, the model is saved as a joblib file (final_model.joblib) inside the` models/` directory for easy reusability.

### Contributing
* Contributions are welcome! If you have any suggestions or improvements, please raise an issue or submit a pull request.

### License
* This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

### Acknowledgments
* Special thanks to the open-source community for the libraries used in this project.