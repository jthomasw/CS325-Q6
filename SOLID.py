#SRP- each class has a single responsibility, such as Console Display 
# which is responsible for displaying data to the console

#OCP- new activites can be created by adding implementations of Activity 
# wihtout having to motify existing classes

#LSP- all Activity subclasses follow the contracts of th eobserver pattern
# making sure that they can be used interchangably with ActivityMoniter

#ISP- seperate interfaces for (DataStorage and Display for example)
# are defined for data storage and display concerns

#DIP- dependencies (DataStorage and Display for example) are injected into 
# the ActivityMoniter class, making it easier to test 


class DataStorage:
    def store_activity_data(self, activity_data: dict):
        raise NotImplementedError("Subclasses must implement store_activity_data method.")


class Display:
    def update(self, activity_data: dict):
        raise NotImplementedError("Subclasses must implement update method.")

class FileDataStorage(DataStorage):
    def store_activity_data(self, activity_data: dict):
        print("Storing activity data in file:", activity_data)

class ConsoleDisplay(Display):
    def update(self, activity_data: dict):
        print("Displaying activity data on console:", activity_data)

class ActivityMonitor:
    def __init__(self, data_storage: DataStorage, displays: list):
        self.data_storage = data_storage
        self.displays = displays

    def collect_activity_data(self, activity_data: dict):
        self.data_storage.store_activity_data(activity_data)
        self.notify_displays(activity_data)

    def notify_displays(self, activity_data: dict):
        for display in self.displays:
            display.update(activity_data)

class Activity:
    def update(self, activity_data: dict):
        raise NotImplementedError("Subclasses must implement update method.")

class StepsActivity(Activity):
    def update(self, activity_data: dict):
        print("Updating steps activity:", activity_data)


class DistanceActivity(Activity):
    def update(self, activity_data: dict):
        print("Updating distance activity:", activity_data)

class CaloriesActivity(Activity):
    def update(self, activity_data: dict):
        print("Updating calories activity:", activity_data)

def main():
    data_storage = FileDataStorage()
    displays = [ConsoleDisplay()]

    activity_monitor = ActivityMonitor(data_storage, displays)

    activity_data = {"steps": 1000, "distance": 2.5, "calories": 150}
    activity_monitor.collect_activity_data(activity_data)

if __name__ == "__main__":
    main()