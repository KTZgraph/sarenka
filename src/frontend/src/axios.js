
import axios from 'axios';

//baseURL gdize URL musi byc z wielkich liter
const baseURL = 'http://127.0.0.1:8000/api/';

const axiosInstance = axios.create({
  baseURL: baseURL,
  timeout: 5000,
});