import { API_CONFIG, ERROR_MESSAGES } from '../utils/constants';

class APIError extends Error {
  constructor(message, status, data = null) {
    super(message);
    this.name = 'APIError';
    this.status = status;
    this.data = data;
  }
}

class PortfolioAPI {
  static baseURL = API_CONFIG.BASE_URL;
  static timeout = API_CONFIG.TIMEOUT;

  /**
   * Generic fetch wrapper with error handling and timeouts
   */
  static async fetchWithTimeout(url, options = {}) {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), this.timeout);

    try {
      const response = await fetch(url, {
        ...options,
        signal: controller.signal,
        headers: {
          'Content-Type': 'application/json',
          ...options.headers,
        },
      });

      clearTimeout(timeoutId);

      if (!response.ok) {
        const errorData = await response.text();
        let parsedError;
        
        try {
          parsedError = JSON.parse(errorData);
        } catch {
          parsedError = { message: errorData || response.statusText };
        }

        throw new APIError(
          parsedError.detail || parsedError.message || `HTTP ${response.status}`,
          response.status,
          parsedError
        );
      }

      return await response.json();
    } catch (error) {
      clearTimeout(timeoutId);
      
      if (error.name === 'AbortError') {
        throw new APIError(ERROR_MESSAGES.TIMEOUT_ERROR, 408);
      }
      
      if (error instanceof APIError) {
        throw error;
      }
      
      // Network or other errors
      throw new APIError(ERROR_MESSAGES.NETWORK_ERROR, 0, error);
    }
  }

  /**
   * Retry wrapper for failed requests
   */
  static async withRetry(requestFn, retries = API_CONFIG.RETRY_ATTEMPTS) {
    try {
      return await requestFn();
    } catch (error) {
      if (retries > 0 && error.status >= 500) {
        await new Promise(resolve => setTimeout(resolve, API_CONFIG.RETRY_DELAY));
        return this.withRetry(requestFn, retries - 1);
      }
      throw error;
    }
  }

  // ========================
  // Portfolio Endpoints
  // ========================

  /**
   * Get complete portfolio data
   */
  static async fetchPortfolio() {
    return this.withRetry(() => 
      this.fetchWithTimeout(`${this.baseURL}/portfolio`)
    );
  }

  /**
   * Update personal information
   */
  static async updatePersonalInfo(updates) {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/portfolio/personal`, {
        method: 'PUT',
        body: JSON.stringify(updates),
      })
    );
  }

  /**
   * Update about section
   */
  static async updateAboutSection(updates) {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/portfolio/about`, {
        method: 'PUT',
        body: JSON.stringify(updates),
      })
    );
  }

  // ========================
  // Skills Endpoints
  // ========================

  /**
   * Get all skill categories
   */
  static async fetchSkills() {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/skills`)
    );
  }

  /**
   * Create new skill category
   */
  static async createSkill(skillData) {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/skills`, {
        method: 'POST',
        body: JSON.stringify(skillData),
      })
    );
  }

  /**
   * Update skill category
   */
  static async updateSkill(skillId, updates) {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/skills/${skillId}`, {
        method: 'PUT',
        body: JSON.stringify(updates),
      })
    );
  }

  /**
   * Delete skill category
   */
  static async deleteSkill(skillId) {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/skills/${skillId}`, {
        method: 'DELETE',
      })
    );
  }

  // ========================
  // Experience Endpoints
  // ========================

  /**
   * Get all experiences
   */
  static async fetchExperiences() {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/experience`)
    );
  }

  /**
   * Create new experience
   */
  static async createExperience(expData) {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/experience`, {
        method: 'POST',
        body: JSON.stringify(expData),
      })
    );
  }

  /**
   * Update experience
   */
  static async updateExperience(expId, updates) {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/experience/${expId}`, {
        method: 'PUT',
        body: JSON.stringify(updates),
      })
    );
  }

  /**
   * Delete experience
   */
  static async deleteExperience(expId) {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/experience/${expId}`, {
        method: 'DELETE',
      })
    );
  }

  // ========================
  // Projects Endpoints
  // ========================

  /**
   * Get all projects
   */
  static async fetchProjects() {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/projects`)
    );
  }

  /**
   * Create new project
   */
  static async createProject(projectData) {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/projects`, {
        method: 'POST',
        body: JSON.stringify(projectData),
      })
    );
  }

  /**
   * Update project
   */
  static async updateProject(projectId, updates) {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/projects/${projectId}`, {
        method: 'PUT',
        body: JSON.stringify(updates),
      })
    );
  }

  /**
   * Delete project
   */
  static async deleteProject(projectId) {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/projects/${projectId}`, {
        method: 'DELETE',
      })
    );
  }

  // ========================
  // Achievements Endpoints
  // ========================

  /**
   * Get all achievements
   */
  static async fetchAchievements() {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/achievements`)
    );
  }

  /**
   * Create new achievement
   */
  static async createAchievement(achievementData) {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/achievements`, {
        method: 'POST',
        body: JSON.stringify(achievementData),
      })
    );
  }

  /**
   * Update achievement
   */
  static async updateAchievement(achievementId, updates) {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/achievements/${achievementId}`, {
        method: 'PUT',
        body: JSON.stringify(updates),
      })
    );
  }

  /**
   * Delete achievement
   */
  static async deleteAchievement(achievementId) {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/achievements/${achievementId}`, {
        method: 'DELETE',
      })
    );
  }

  // ========================
  // Publications Endpoints
  // ========================

  /**
   * Get all publications
   */
  static async fetchPublications() {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/publications`)
    );
  }

  /**
   * Create new publication
   */
  static async createPublication(pubData) {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/publications`, {
        method: 'POST',
        body: JSON.stringify(pubData),
      })
    );
  }

  /**
   * Update publication
   */
  static async updatePublication(pubId, updates) {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/publications/${pubId}`, {
        method: 'PUT',
        body: JSON.stringify(updates),
      })
    );
  }

  /**
   * Delete publication
   */
  static async deletePublication(pubId) {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/publications/${pubId}`, {
        method: 'DELETE',
      })
    );
  }

  // ========================
  // Migration & Export
  // ========================

  /**
   * Migrate mock data to database
   */
  static async migrateMockData(mockData) {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/migrate`, {
        method: 'POST',
        body: JSON.stringify(mockData),
      })
    );
  }

  /**
   * Export all portfolio data
   */
  static async exportData() {
    return this.withRetry(() =>
      this.fetchWithTimeout(`${this.baseURL}/export`)
    );
  }

  // ========================
  // Utility Methods
  // ========================

  /**
   * Health check endpoint
   */
  static async healthCheck() {
    try {
      const response = await fetch(`${this.baseURL}/`, {
        method: 'GET',
        timeout: 5000,
      });
      return response.ok;
    } catch {
      return false;
    }
  }

  /**
   * Get API status
   */
  static async getStatus() {
    return this.fetchWithTimeout(`${this.baseURL}/status`);
  }
}

export { PortfolioAPI, APIError };
export default PortfolioAPI;