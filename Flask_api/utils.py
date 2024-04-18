import numpy as np
import pandas as pd
import pickle 
import config 
import json


class MbaMarks():
    def __init__(self, ssc_percentage,hsc_percentage,degree_percentage,
                work_experience, emp_test_percentage,specialisation,status):
                self.ssc_percentage = ssc_percentage
                self.hsc_percentage = hsc_percentage
                self.degree_percentage = degree_percentage
                self.work_experience = work_experience
                self.emp_test_percentage = emp_test_percentage
                self.specialisation = specialisation
                self.status = status
 
    def load_model(self):
        with open(config.model_filepath,"rb")as fp:
            self.model = pickle.load(fp)
        with open(config.json_path,"r") as fp:
            self.json_data = json.load(fp)

    def mba_percentage_calc(self):
        self.load_model()
        test_array = np.zeros(len(self.json_data["columns"]))
        test_array[0] = self.ssc_percentage
        test_array[1] = self.hsc_percentage
        test_array[2] = self.degree_percentage
        test_array[3] = self.json_data["work_experience"][self.work_experience]
        test_array[4] = self.emp_test_percentage
        test_array[5] = self.json_data["specialisation"][self.specialisation]
        test_array[6] = self.json_data["status"][self.status]

        print('test_array', test_array)

        predicted_marks = np.around(self.model.predict([test_array])[0],2)
        print(predicted_marks)
        return predicted_marks
        
if __name__ == "__main__":
    ssc_percentage = 65.00
    hsc_percentage = 68.00
    degree_percentage= 64.00
    work_experience = 0
    emp_test_percentage = 75.00
    specialisation = 0
    status = 0

    mba = MbaMarks(ssc_percentage,hsc_percentage,degree_percentage,
                work_experience, emp_test_percentage,specialisation,status)

    mba.mba_percentage_calc()



