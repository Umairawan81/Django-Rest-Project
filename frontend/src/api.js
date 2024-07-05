import axios from 'axios';
import { ACCESS_TOKEN } from './constants';

const api = axios.create({
    baseURL: import.meta.env.VITE_APP_URL
});

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        console.log('Retrieved token:', token); // Log token retrieval
        if (token) {
            config.headers.Authorization = `Bearer ${token}`; // Ensure "Bearer" is capitalized
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export default api;
