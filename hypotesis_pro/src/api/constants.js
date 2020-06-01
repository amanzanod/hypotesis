//const HYPOTESIS_MANAGER_URL = 'http://127.0.0.1:8000/api/';

const HYP_MANAGER_URL = process.env.HYP_MANAGER_URL;

let manager_url = '';

if (HYP_MANAGER_URL) {
    manager_url = 'http://' + HYP_MANAGER_URL + '/api/';
} else {
    manager_url = 'http://192.168.99.100:8000/api/';
}

const HYP_MANAGER_USER = manager_url + 'user/';
const HYP_MANAGER_ROLE = manager_url + 'role/';
const HYP_MANAGER_PROVINCE = manager_url + 'province/';
const HYP_MANAGER_COUNTRY = manager_url + 'country/';
const HYP_MANAGER_STATE = manager_url + 'state/';
const HYP_MANAGER_LANGUAGE = manager_url + 'language/';
const HYP_MANAGER_PERMISSION = manager_url + 'permission/';
const HYP_MANAGER_CONTEXT= manager_url + 'context/';


const HYPOTESIS_CONTEXT_URL = 'http://192.168.99.100:8001/api/';
const HYP_MANAGER_GRADE= HYPOTESIS_CONTEXT_URL + 'grade/';
const HYP_MANAGER_COURSE= HYPOTESIS_CONTEXT_URL + 'course/';

export {
    HYP_MANAGER_USER,
    HYP_MANAGER_ROLE,
    HYP_MANAGER_PERMISSION,
    HYP_MANAGER_CONTEXT,
    HYP_MANAGER_PROVINCE,
    HYP_MANAGER_COUNTRY,
    HYP_MANAGER_STATE,
    HYP_MANAGER_LANGUAGE,
    HYP_MANAGER_GRADE,
    HYP_MANAGER_COURSE
};
