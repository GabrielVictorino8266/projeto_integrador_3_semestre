import axios from 'axios';

// export const api = axios.create({
//   baseURL: 'http://localhost:8000/api'
// });

export const api = axios.create({
  baseURL: 'https://projeto-integrador-3-semestre.onrender.com'
});

api.interceptors.request.use((config) => {
  if (config.url?.includes('/users/login/')) {
    return config;
  }

  if (config.url?.includes('/users/refresh-token/')) {
    return config;
  }

  const token = localStorage.getItem('token');

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});
