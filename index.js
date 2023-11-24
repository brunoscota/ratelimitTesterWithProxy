const axios = require('axios');

// Read environment variables
const testedUrl = process.env.TESTED_URL;
const rateLimit = parseInt(process.env.RATE_LIMIT || '100', 10); // Convert RATE_LIMIT to integer
const interval = parseFloat(process.env.INTERVAL || (60 / rateLimit)); // Convert INTERVAL to float

// Function to send requests
async function sendRequest() {
  try {
    const response = await axios.get(testedUrl);
    return response.status;
  } catch (error) {
    console.error('Error in request:', error);
    return error.response ? error.response.status : 'No response';
  }
}

// Main loop
(async () => {
  for (let i = 0; i < rateLimit; i++) {
    const status = await sendRequest();
    console.log(`Request ${i + 1}, Status Code: ${status}`);
    await new Promise(resolve => setTimeout(resolve, interval * 1000));
  }
})();
