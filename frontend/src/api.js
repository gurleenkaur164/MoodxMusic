import axios from 'axios';

const API= axios.create({
    baseURL: 'http://localhost:8000',
});

export const getMood=(text) => {
    return API.post('/predict', {text});
};