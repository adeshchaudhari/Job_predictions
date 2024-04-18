from flask import Flask, request, jsonify
import utils

app = Flask(__name__)

@app.route('/', methods = ["GET"])
def get_mba_percentage():
    if request.method == 'GET':
        data = request.form
        ssc_percentage = eval(data["ssc_percentage"])
        hsc_percentage = eval(data["hsc_percentage"])
        degree_percentage = eval(data["degree_percentage"])
        work_experience = eval(data["work-experience"])
        emp_test_percentage = eval(data["emp_test_percentage"])
        specialisation = eval(data["specialisation"])
        status = eval(data["status"])

        mba_percent = utils.MbaMarks(ssc_percentage,hsc_percentage,degree_percentage,
                work_experience, emp_test_percentage,specialisation,status)

        mba_percentage = mba_percent.mba_percentage_calc()
        return jsonify({"percentage are": mba_percentage})
    
app.run()
