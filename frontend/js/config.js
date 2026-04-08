// Centralized API Configuration for Hospital Monitoring System
// This ensures ALL pages point to the correct backend, whether local or deployed.

const API_CONFIG = (() => {
    const hostname = window.location.hostname;

    // Local development
    if (hostname === 'localhost' || hostname === '127.0.0.1') {
        return { BASE_URL: 'http://localhost:5000' };
    }

    // If served directly from Render backend (same origin)
    if (hostname.includes('.onrender.com')) {
        return { BASE_URL: '' }; // relative path works since backend serves frontend
    }

    // Deployed on Vercel or any other external host — point to Render backend
    return { BASE_URL: 'https://anamoly-detection-1.onrender.com' };
})();
