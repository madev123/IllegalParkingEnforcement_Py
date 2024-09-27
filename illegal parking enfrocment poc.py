# ParkingIncident Class
class ParkingIncident:
    def __init__(self, incident_id, vehicle_number, date, location, violation_type):
        self.incident_id = incident_id
        self.vehicle_number = vehicle_number
        self.date = date
        self.location = location
        self.violation_type = violation_type

    def __repr__(self):
        return f"ParkingIncident({self.incident_id}, {self.vehicle_number}, {self.date}, {self.location}, {self.violation_type})"


# TowingOperation Class
class TowingOperation:
    def __init__(self, operation_id, vehicle_number, date, location):
        self.operation_id = operation_id
        self.vehicle_number = vehicle_number
        self.date = date
        self.location = location

    def __repr__(self):
        return f"TowingOperation({self.operation_id}, {self.vehicle_number}, {self.date}, {self.location})"


# Parking Enforcement System Class
class ParkingEnforcementSystem:
    def __init__(self):
        self.parking_incidents = []
        self.towing_operations = []

    # CRUD for ParkingIncident
    def record_illegal_parking(self, incident):
        self.parking_incidents.append(incident)

    def get_parking_incident(self, incident_id):
        for incident in self.parking_incidents:
            if incident.incident_id == incident_id:
                return incident
        return None

    def update_parking_incident(self, incident_id, new_incident):
        for i, incident in enumerate(self.parking_incidents):
            if incident.incident_id == incident_id:
                self.parking_incidents[i] = new_incident
                return True
        return False

    def delete_parking_incident(self, incident_id):
        for i, incident in enumerate(self.parking_incidents):
            if incident.incident_id == incident_id:
                del self.parking_incidents[i]
                return True
        return False

    # CRUD for TowingOperation
    def manage_towing_operations(self, towing_op):
        self.towing_operations.append(towing_op)

    def get_towing_operation(self, operation_id):
        for operation in self.towing_operations:
            if operation.operation_id == operation_id:
                return operation
        return None

    def update_towing_operation(self, operation_id, new_operation):
        for i, operation in enumerate(self.towing_operations):
            if operation.operation_id == operation_id:
                self.towing_operations[i] = new_operation
                return True
        return False

    def delete_towing_operation(self, operation_id):
        for i, operation in enumerate(self.towing_operations):
            if operation.operation_id == operation_id:
                del self.towing_operations[i]
                return True
        return False


# Unit Tests
import unittest

class TestParkingEnforcementSystem(unittest.TestCase):
    def setUp(self):
        self.system = ParkingEnforcementSystem()

    def test_record_illegal_parking(self):
        incident = ParkingIncident(1, 'ABC123', '2024-09-25', 'Downtown', 'No Parking Zone')
        self.system.record_illegal_parking(incident)
        self.assertIn(incident, self.system.parking_incidents)

    def test_manage_towing_operations(self):
        towing_op = TowingOperation(1, 'XYZ789', '2024-09-25', 'Uptown')
        self.system.manage_towing_operations(towing_op)
        self.assertIn(towing_op, self.system.towing_operations)

    def test_update_parking_incident(self):
        incident = ParkingIncident(1, 'ABC123', '2024-09-25', 'Downtown', 'No Parking Zone')
        self.system.record_illegal_parking(incident)
        new_incident = ParkingIncident(1, 'ABC123', '2024-09-26', 'Downtown', 'Expired Meter')
        self.assertTrue(self.system.update_parking_incident(1, new_incident))
        self.assertEqual(self.system.get_parking_incident(1).violation_type, 'Expired Meter')

    def test_delete_parking_incident(self):
        incident = ParkingIncident(1, 'ABC123', '2024-09-25', 'Downtown', 'No Parking Zone')
        self.system.record_illegal_parking(incident)
        self.assertTrue(self.system.delete_parking_incident(1))
        self.assertIsNone(self.system.get_parking_incident(1))

    def test_update_towing_operation(self):
        towing_op = TowingOperation(1, 'XYZ789', '2024-09-25', 'Uptown')
        self.system.manage_towing_operations(towing_op)
        new_towing_op = TowingOperation(1, 'XYZ789', '2024-09-26', 'Downtown')
        self.assertTrue(self.system.update_towing_operation(1, new_towing_op))
        self.assertEqual(self.system.get_towing_operation(1).location, 'Downtown')

    def test_delete_towing_operation(self):
        towing_op = TowingOperation(1, 'XYZ789', '2024-09-25', 'Uptown')
        self.system.manage_towing_operations(towing_op)
        self.assertTrue(self.system.delete_towing_operation(1))
        self.assertIsNone(self.system.get_towing_operation(1))

if __name__ == '__main__':
    unittest.main()
