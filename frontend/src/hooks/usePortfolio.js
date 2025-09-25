import { useState, useEffect, useCallback } from 'react';
import { PortfolioAPI, APIError } from '../services/api';
import { ERROR_MESSAGES, CACHE_CONFIG } from '../utils/constants';

/**
 * Custom hook for managing portfolio data
 */
export const usePortfolio = () => {
  const [portfolioData, setPortfolioData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [lastFetched, setLastFetched] = useState(null);

  // Cache management
  const isCacheValid = useCallback(() => {
    if (!lastFetched) return false;
    return Date.now() - lastFetched < CACHE_CONFIG.PORTFOLIO_TTL;
  }, [lastFetched]);

  /**
   * Fetch portfolio data
   */
  const fetchPortfolio = useCallback(async (forceRefresh = false) => {
    // Return cached data if valid and not forcing refresh
    if (!forceRefresh && portfolioData && isCacheValid()) {
      return portfolioData;
    }

    try {
      setLoading(true);
      setError(null);
      
      const data = await PortfolioAPI.fetchPortfolio();
      
      setPortfolioData(data);
      setLastFetched(Date.now());
      setError(null);
      
      return data;
    } catch (err) {
      const errorMessage = err instanceof APIError 
        ? err.message 
        : ERROR_MESSAGES.UNKNOWN_ERROR;
      
      setError(errorMessage);
      console.error('Portfolio fetch error:', err);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [portfolioData, isCacheValid]);

  /**
   * Refresh portfolio data
   */
  const refresh = useCallback(() => {
    return fetchPortfolio(true);
  }, [fetchPortfolio]);

  /**
   * Update personal information
   */
  const updatePersonalInfo = useCallback(async (updates) => {
    try {
      setLoading(true);
      await PortfolioAPI.updatePersonalInfo(updates);
      
      // Update local state
      setPortfolioData(prev => ({
        ...prev,
        portfolio: {
          ...prev.portfolio,
          personal: {
            ...prev.portfolio.personal,
            ...updates
          }
        }
      }));
      
      return true;
    } catch (err) {
      const errorMessage = err instanceof APIError 
        ? err.message 
        : ERROR_MESSAGES.UNKNOWN_ERROR;
      setError(errorMessage);
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  /**
   * Update about section
   */
  const updateAboutSection = useCallback(async (updates) => {
    try {
      setLoading(true);
      await PortfolioAPI.updateAboutSection(updates);
      
      // Update local state
      setPortfolioData(prev => ({
        ...prev,
        portfolio: {
          ...prev.portfolio,
          about: {
            ...prev.portfolio.about,
            ...updates
          }
        }
      }));
      
      return true;
    } catch (err) {
      const errorMessage = err instanceof APIError 
        ? err.message 
        : ERROR_MESSAGES.UNKNOWN_ERROR;
      setError(errorMessage);
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  // Initial fetch on mount
  useEffect(() => {
    fetchPortfolio();
  }, [fetchPortfolio]);

  return {
    // Data
    portfolioData,
    portfolio: portfolioData?.portfolio,
    skills: portfolioData?.skills || [],
    experiences: portfolioData?.experiences || [],
    projects: portfolioData?.projects || [],
    achievements: portfolioData?.achievements || [],
    publications: portfolioData?.publications || [],
    
    // State
    loading,
    error,
    lastFetched,
    
    // Methods
    fetchPortfolio,
    refresh,
    updatePersonalInfo,
    updateAboutSection,
    
    // Utilities
    isCacheValid: isCacheValid(),
    hasData: !!portfolioData,
  };
};

/**
 * Hook for individual data sections
 */
export const usePortfolioSection = (section) => {
  const { portfolioData, loading, error, refresh } = usePortfolio();
  
  return {
    data: portfolioData?.[section] || [],
    loading,
    error,
    refresh,
  };
};

/**
 * Hook for API status monitoring
 */
export const useAPIStatus = () => {
  const [isOnline, setIsOnline] = useState(true);
  const [apiHealthy, setApiHealthy] = useState(true);

  const checkAPIHealth = useCallback(async () => {
    try {
      const healthy = await PortfolioAPI.healthCheck();
      setApiHealthy(healthy);
      return healthy;
    } catch {
      setApiHealthy(false);
      return false;
    }
  }, []);

  useEffect(() => {
    // Check network status
    const handleOnline = () => setIsOnline(true);
    const handleOffline = () => setIsOnline(false);

    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);

    // Initial API health check
    checkAPIHealth();

    // Periodic health checks
    const healthCheckInterval = setInterval(checkAPIHealth, 30000); // 30 seconds

    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
      clearInterval(healthCheckInterval);
    };
  }, [checkAPIHealth]);

  return {
    isOnline,
    apiHealthy,
    checkAPIHealth,
    isConnected: isOnline && apiHealthy,
  };
};

export default usePortfolio;