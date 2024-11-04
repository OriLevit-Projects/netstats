<template>
  <div class="app">
    <nav class="navbar">
      <router-link to="/" class="nav-logo">
        Volleyball Stats
      </router-link>
      
      <div class="nav-links">
        <!-- Show these links when user is NOT logged in -->
        <template v-if="!isLoggedIn">
          <router-link to="/login">Login</router-link>
          <router-link to="/signup">Sign Up</router-link>
        </template>
        
        <!-- Show these links when user IS logged in -->
        <template v-if="isLoggedIn">
          <router-link to="/dashboard">Dashboard</router-link>
          <router-link to="/profile">Profile</router-link>
          <a href="#" @click.prevent="handleLogout" class="logout-btn">Logout</a>
        </template>
      </div>
    </nav>
    
    <main>
      <router-view></router-view>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { authApi } from './services/api'

const router = useRouter()
const isLoggedIn = ref(false)

// Check auth status on component mount
onMounted(() => {
  checkAuthStatus()
})

// Function to check if user is logged in
const checkAuthStatus = () => {
  const token = localStorage.getItem('token')
  isLoggedIn.value = !!token
}

// Handle logout
const handleLogout = () => {
  authApi.logout()
  isLoggedIn.value = false
  router.push('/login')
}

// Watch for route changes to recheck auth status
router.beforeEach((to, from, next) => {
  checkAuthStatus()
  next()
})
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  min-width: 100vw;
  min-height: 100vh;
  overflow-x: hidden;
}

.app {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.navbar {
  width: 100%;
  height: 80px;
  background-color: #2c3e50;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 5%;
}

.nav-logo {
  font-size: 24px;
  color: white;
  text-decoration: none;
  font-weight: bold;
}

.nav-links {
  display: flex;
  gap: 2rem;
}

.nav-links a {
  color: white;
  text-decoration: none;
  font-size: 16px;
  padding: 8px 16px;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.nav-links a:hover {
  background-color: #34495e;
}

.logout-btn {
  cursor: pointer;
}

.logout-btn:hover {
  background-color: #c0392b !important;
}

main {
  flex: 1;
  width: 100%;
  padding: 0;
  margin: 0;
}
</style>