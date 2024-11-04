import axios from 'axios'

const api = axios.create({
    baseURL: 'http://localhost:8000/api',
    headers: {
        'Content-Type': 'application/json',
    },
})

export const authApi = {
    login: async (email: string, password: string) => {
    try {
        console.log('Attempting login with:', { email }) // Add this line
        
        const formData = new FormData()
        formData.append('username', email)
        formData.append('password', password)
        
        const response = await api.post('/auth/token', formData, {
            headers: {
                'Content-Type': 'multipart/form-data', // Add this line
            },
        })
        console.log('Login response:', response.data) // Add this line
        return response.data
    } catch (error: any) {
        console.error('Login error:', error) // Add this line
        
        if (error.response?.status === 401) {
            throw new Error('Invalid email or password')
        } else if (error.response?.status === 422) {
            throw new Error('Please check your email and password format')
        } else if (!error.response) {
            throw new Error('Network error. Please check your connection.')
        }
        throw error
    }
},

    signup: async (username: string, email: string, password: string) => {
        try {
            const response = await api.post('/auth/signup', {
                username,
                email,
                password,
            })
            return response.data
        } catch (error: any) {
            if (error.response?.status === 400) {
                throw new Error('Email already registered')
            } else if (error.response?.status === 422) {
                throw new Error('Please check your input format')
            } else if (!error.response) {
                throw new Error('Network error. Please check your connection.')
            }
            throw error
        }
    },

    // Get current user profile
    getProfile: async () => {
        try {
            const token = localStorage.getItem('token')
            if (!token) {
                throw new Error('No authentication token found')
            }

            const response = await api.get('/auth/profile', {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            })
            return response.data
        } catch (error: any) {
            if (error.response?.status === 401) {
                throw new Error('Session expired. Please login again.')
            }
            throw error
        }
    },

    // Logout
    logout: () => {
        localStorage.removeItem('token')
    }
}

// Add axios interceptor to handle errors globally
api.interceptors.response.use(
    (response) => response,
    (error) => {
        if (error.response?.status === 401) {
            // Clear token and redirect to login if session is expired
            localStorage.removeItem('token')
            window.location.href = '/login'
        }
        return Promise.reject(error)
    }
)

// Add axios interceptor to add token to requests
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('token')
        if (token) {
            config.headers.Authorization = `Bearer ${token}`
        }
        return config
    },
    (error) => {
        return Promise.reject(error)
    }
)

export default api