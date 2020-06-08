const HYP_LOCAL_IP = '192.168.99.100';

let manager_url = 'http://' + HYP_LOCAL_IP + ':8000/api/';
let context_url = 'http://' + HYP_LOCAL_IP + ':8001/api/';
//let item_url = 'http://' + HYP_LOCAL_IP + ':8002/api/';
let enrol_url = 'http://' + HYP_LOCAL_IP + ':8003/api/';


const HYP_MANAGER_USER = manager_url + 'user/';
const HYP_MANAGER_ROLE = manager_url + 'role/';
const HYP_MANAGER_PROVINCE = manager_url + 'province/';
const HYP_MANAGER_STATE = manager_url + 'state/';
const HYP_MANAGER_LANGUAGE = manager_url + 'language/';
const HYP_MANAGER_PERMISSION = manager_url + 'permission/';
const HYP_MANAGER_ROLEPERMISSION = manager_url + 'permissionrole/';
const HYP_MANAGER_CONTEXT= manager_url + 'context/';

const HYP_CONTEXT_GRADE = context_url + 'grade/';
const HYP_CONTEXT_MASTER = context_url + 'master/';
const HYP_CONTEXT_COURSE = context_url + 'course/';
const HYP_CONTEXT_CLASSROOM = context_url + 'classroom/';
const HYP_CONTEXT_CATEGORY = context_url + 'category/';
const HYP_CONTEXT_STATE = context_url + 'state/';
const HYP_CONTEXT_FORMAT = context_url + 'format/';
const HYP_CONTEXT_LANGUAGE = context_url + 'language/';
const HYP_CONTEXT_LEVEL = context_url + 'level/';

//const HYP_ITEM_ITEM = item_url + 'item/';
const HYP_ENROL_ENROL = enrol_url + 'enrol/';

export {
    HYP_MANAGER_USER,
    HYP_MANAGER_ROLE,
    HYP_MANAGER_PERMISSION,
    HYP_MANAGER_CONTEXT,
    HYP_MANAGER_PROVINCE,
    HYP_MANAGER_STATE,
    HYP_MANAGER_LANGUAGE,
    HYP_CONTEXT_GRADE,
    HYP_CONTEXT_MASTER,
    HYP_CONTEXT_COURSE,
    HYP_CONTEXT_CLASSROOM,
    HYP_CONTEXT_CATEGORY,
    HYP_MANAGER_ROLEPERMISSION,
    HYP_CONTEXT_STATE,
    HYP_CONTEXT_FORMAT,
    HYP_CONTEXT_LANGUAGE,
    HYP_CONTEXT_LEVEL,
    //HYP_ITEM_ITEM,
    HYP_ENROL_ENROL
};
