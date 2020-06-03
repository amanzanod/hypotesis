//const HYPOTESIS_MANAGER_URL = 'http://127.0.0.1:8000/api/';

const HYP_MANAGER_URL = process.env.HYP_MANAGER_URL;
const HYP_CONTEXT_URL = process.env.HYP_CONTEXT_URL;
const HYP_ITEM_URL = process.env.HYP_ITEM_URL;
const HYP_ENROL_URL = process.env.HYP_ENROL_URL;
console.log(HYP_MANAGER_URL);
console.log(HYP_CONTEXT_URL);
console.log(HYP_ITEM_URL);
console.log(HYP_ENROL_URL);

let manager_url = '';
let context_url = '';

if (HYP_MANAGER_URL) {
    manager_url = 'http://' + HYP_MANAGER_URL + '/api/';
} else {
    manager_url = 'http://192.168.99.100:8000/api/';
}

if (HYP_CONTEXT_URL) {
    context_url = 'http://' + HYP_MANAGER_URL + '/api/';
} else {
    context_url = 'http://192.168.99.100:8001/api/';
}

const HYP_MANAGER_USER = manager_url + 'user/';
const HYP_MANAGER_ROLE = manager_url + 'role/';
const HYP_MANAGER_PROVINCE = manager_url + 'province/';
const HYP_MANAGER_COUNTRY = manager_url + 'country/';
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

export {
    HYP_MANAGER_USER,
    HYP_MANAGER_ROLE,
    HYP_MANAGER_PERMISSION,
    HYP_MANAGER_CONTEXT,
    HYP_MANAGER_PROVINCE,
    HYP_MANAGER_COUNTRY,
    HYP_MANAGER_STATE,
    HYP_MANAGER_LANGUAGE,
    HYP_CONTEXT_GRADE,
    HYP_CONTEXT_MASTER,
    HYP_CONTEXT_COURSE,
    HYP_CONTEXT_CLASSROOM,
    HYP_CONTEXT_CATEGORY,
    HYP_MANAGER_ROLEPERMISSION
};
