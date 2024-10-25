import axios  from 'axios';

const instance = axios.create();
instance.defaults.timeout = 5000;
instance.defaults.baseURL = "http://0.0.0.0:8000"
instance.defaults.headers.post['Content-Type'] = 'application/json';
instance.defaults.headers.post['Accept'] = 'application/json'

export default instance