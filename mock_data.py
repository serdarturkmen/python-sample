import csv

data = []


def get_data():
    with open('app/mock_data.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            data.append(
                {
                    "airportArrival": row["Airport Arrival"],
                    "airportDepature": row["Airport Depature"],
                    "combinedError": row["Combined Error (Avg of Labeled - Predicted)"],
                    "combinedErrorInPercent": row["Combined Error %"],
                    "combinedLabeledAvg": row["Combined Labeled Avg"],
                    "combinedPredictedAvg": row["Combined Predicted Avg"],
                    "cruiseTime": row["CruiseTime (hrs.)"],
                    "engineFourError": row["Engine 4 Error (Avg of Labeled - Predicted)"],
                    "engineFourErrorInPercent": row["Engine 4 Error %"],
                    "engineFourLabeledAvg": row["Engine 4 Labeled Avg"],
                    "engineFourPredictedAvg": row["Engine 4 Predicted Avg"],
                    "engineOneError": row["Engine 1 Error (Avg of Labeled - Predicted)"],
                    "engineOneErrorInPercent": row["Engine 1 Error %"],
                    "engineOneLabeledAvg": row["Engine 1 Labeled Avg"],
                    "engineOnePredictedAvg": row["Engine 1 Predicted Avg"],
                    "engineThreeError": row["Engine 3 Error (Avg of Labeled - Predicted)"],
                    "engineThreeErrorInPercent": row["Engine 3 Error %"],
                    "engineThreeLabeledAvg": row["Engine 3 Labeled Avg"],
                    "engineThreePredictedAvg": row["Engine 3 Predicted Avg"],
                    "engineTwoError": row["Engine 2 Error (Avg of Labeled - Predicted)"],
                    "engineTwoErrorInPercent": row["Engine 2 Error %"],
                    "engineTwoLabeledAvg": row["Engine 2 Labeled Avg"],
                    "engineTwoPredictedAvg": row["Engine 2 Predicted Avg"],
                    "flightTime": row["FlightTime (hrs.)"],
                    "flightcycle": row["Flightcount"],
                    "flightnumber": row["Flightnumber"],
                    "grossWeight": row["GrossWeight"],
                    "rmseFour": row["rmse 4"],
                    "rmseOne": row["rmse 1"],
                    "rmseThree": row["rmse 3"],
                    "rmseTwo": row["rmse 2"],
                    "timestampStartOfFlight": row["Timestamp Start of Flight"],
                    "id": line_count
                }
            )
            line_count += 1
        print(f'Processed {line_count} lines.')
    return data
