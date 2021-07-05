studentSchema = {
    "properties": {
        "rNo": { "type": "string" },
        "firstName": { "type": "string" },
        "lastName": { "type": "string" },
        "dept": { "type": "string" }
    },
    "required": [ "rNo", "firstName", "lastName", "dept" ]
}

departmentSchema = {
    "properties": {
        "deptCode": { "type": "string" },
        "deptName": { "type": "string" },
    },
    "required": [ "deptCode", "deptName" ]
}