import React, { useState, useEffect } from 'react';
import { useSearchParams } from 'react-router-dom';
import InvestmentCard from './InvestmentCard';
import InvestmentSummary from './InvestmentSummary';

const InvestmentsPage = () => {
  const [recommendations, setRecommendations] = useState([]);
  const [summary, setSummary] = useState(null);
  const [assetTypes, setAssetTypes] = useState([]);
  const [selectedAssetType, setSelectedAssetType] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchParams, setSearchParams] = useSearchParams();

  const backendUrl = process.env.REACT_APP_BACKEND_URL || import.meta.env.REACT_APP_BACKEND_URL;

  useEffect(() => {
    fetchSummary();
    fetchAssetTypes();
    // Get asset type from URL params
    const assetTypeFromUrl = searchParams.get('asset_type');
    if (assetTypeFromUrl) {
      setSelectedAssetType(assetTypeFromUrl);
    }
  }, []);

  useEffect(() => {
    fetchRecommendations();
  }, [selectedAssetType]);

  const fetchSummary = async () => {
    try {
      const response = await fetch(`${backendUrl}/api/investments/summary`);
      if (!response.ok) throw new Error('Failed to fetch summary');
      const data = await response.json();
      setSummary(data);
    } catch (err) {
      console.error('Error fetching summary:', err);
    }
  };

  const fetchAssetTypes = async () => {
    try {
      const response = await fetch(`${backendUrl}/api/investments/types/list`);
      if (!response.ok) throw new Error('Failed to fetch asset types');
      const data = await response.json();
      setAssetTypes(data);
    } catch (err) {
      console.error('Error fetching asset types:', err);
    }
  };

  const fetchRecommendations = async () => {
    try {
      setLoading(true);
      const url = selectedAssetType 
        ? `${backendUrl}/api/investments?asset_type=${encodeURIComponent(selectedAssetType)}`
        : `${backendUrl}/api/investments`;
      
      const response = await fetch(url);
      if (!response.ok) throw new Error('Failed to fetch recommendations');
      
      const data = await response.json();
      setRecommendations(data);
      setError(null);
    } catch (err) {
      setError('Failed to load recommendations. Please try again later.');
      console.error('Error fetching recommendations:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleAssetTypeChange = (assetType) => {
    setSelectedAssetType(assetType);
    // Update URL params
    if (assetType) {
      setSearchParams({ asset_type: assetType });
    } else {
      setSearchParams({});
    }
  };

  const getAssetTypeConfig = (assetType) => {
    const configs = {
      'stock': { label: 'Stocks', icon: '📈', color: 'blue' },
      'index': { label: 'Indices', icon: '📊', color: 'purple' },
      'commodity': { label: 'Commodities', icon: '🏅', color: 'orange' }
    };
    return configs[assetType] || { label: assetType, icon: '💼', color: 'gray' };
  };

  const EmptyStateComponent = () => (
    <div className="text-center py-16">
      <div className="w-24 h-24 mx-auto mb-6 bg-gray-800 rounded-full flex items-center justify-center">
        <span className="text-4xl">📊</span>
      </div>
      <h3 className="heading-3 mb-4">No Investment Data Available</h3>
      <p className="text-gray-400 mb-8 max-w-md mx-auto">
        We're currently working on populating our investment database with the latest market analysis and recommendations.
      </p>
      <div className="space-y-4">
        <button
          onClick={fetchRecommendations}
          className="btn btn-primary mr-4"
        >
          🔄 Refresh Data
        </button>
        <p className="text-sm text-gray-500">
          In the meantime, try our <a href="/ask-advisor" className="text-blue-400 hover:text-blue-300">AI Investment Advisor</a> for personalized recommendations
        </p>
      </div>
    </div>
  );

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <div className="container-fluid py-8">
        {/* Header */}
        <div className="mb-12 text-center">
          <h1 className="heading-1 mb-6">Investment Recommendations</h1>
          <p className="text-xl text-secondary max-w-3xl mx-auto">
            Expert analysis and AI-powered predictions for stocks, indices, and commodities. 
            Make informed investment decisions with confidence.
          </p>
        </div>

        {/* Summary Dashboard */}
        {summary && summary.total_recommendations > 0 && (
          <div className="mb-12">
            <InvestmentSummary summary={summary} />
          </div>
        )}

        {/* Asset Type Filter */}
        {assetTypes.length > 0 && (
          <div className="mb-8">
            <h3 className="text-lg font-semibold mb-6 flex items-center">
              <span className="mr-2">🎯</span>
              Filter by Asset Type
            </h3>
            <div className="flex flex-wrap gap-3">
              <button
                onClick={() => handleAssetTypeChange('')}
                className={`flex items-center space-x-2 px-4 py-3 rounded-xl text-sm font-medium transition-all duration-200 ${
                  selectedAssetType === ''
                    ? 'bg-blue-600 text-white shadow-lg'
                    : 'bg-gray-800 text-gray-300 hover:bg-gray-700 hover:text-white'
                }`}
              >
                <span>🎯</span>
                <span>All Recommendations</span>
                <span className="bg-white/20 px-2 py-1 rounded-full text-xs">
                  {summary?.total_recommendations || 0}
                </span>
              </button>
              
              {assetTypes.map((type) => {
                const config = getAssetTypeConfig(type.asset_type);
                return (
                  <button
                    key={type.asset_type}
                    onClick={() => handleAssetTypeChange(type.asset_type)}
                    className={`flex items-center space-x-2 px-4 py-3 rounded-xl text-sm font-medium transition-all duration-200 ${
                      selectedAssetType === type.asset_type
                        ? 'bg-blue-600 text-white shadow-lg'
                        : 'bg-gray-800 text-gray-300 hover:bg-gray-700 hover:text-white'
                    }`}
                  >
                    <span>{config.icon}</span>
                    <span>{config.label}</span>
                    <span className="bg-white/20 px-2 py-1 rounded-full text-xs">
                      {type.count}
                    </span>
                  </button>
                );
              })}
            </div>
          </div>
        )}

        {/* Content */}
        {loading ? (
          <div className="flex justify-center items-center py-20">
            <div className="text-center">
              <div className="w-16 h-16 border-4 border-blue-500 border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
              <p className="text-gray-400">Loading investment recommendations...</p>
            </div>
          </div>
        ) : error ? (
          <div className="text-center py-16">
            <div className="w-16 h-16 mx-auto mb-6 bg-red-600/20 rounded-full flex items-center justify-center">
              <span className="text-2xl">⚠️</span>
            </div>
            <h3 className="text-xl font-semibold text-red-400 mb-4">Error Loading Data</h3>
            <div className="text-gray-400 mb-6">{error}</div>
            <button
              onClick={fetchRecommendations}
              className="btn btn-primary"
            >
              🔄 Try Again
            </button>
          </div>
        ) : recommendations.length === 0 ? (
          <EmptyStateComponent />
        ) : (
          <>
            {/* Results Header */}
            <div className="flex items-center justify-between mb-8">
              <div>
                <h2 className="text-2xl font-semibold text-white">
                  {selectedAssetType ? getAssetTypeConfig(selectedAssetType).label : 'All Recommendations'}
                </h2>
                <p className="text-gray-400">
                  {recommendations.length} recommendation{recommendations.length !== 1 ? 's' : ''} found
                </p>
              </div>
              
              {selectedAssetType && (
                <button
                  onClick={() => handleAssetTypeChange('')}
                  className="btn btn-outline text-sm"
                >
                  ← View All
                </button>
              )}
            </div>

            {/* Investment Cards Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
              {recommendations.map((recommendation, index) => (
                <div 
                  key={recommendation.id}
                  className="animate-fade-in-up"
                  style={{ animationDelay: `${index * 0.1}s` }}
                >
                  <InvestmentCard recommendation={recommendation} />
                </div>
              ))}
            </div>

            {/* Call to Action */}
            <div className="text-center mt-16 py-12 bg-gradient-to-r from-blue-600/10 to-purple-600/10 rounded-2xl">
              <h3 className="text-2xl font-semibold mb-4">Need Personalized Advice?</h3>
              <p className="text-gray-400 mb-6 max-w-2xl mx-auto">
                Get tailored investment recommendations and real-time market analysis from our AI advisor.
              </p>
              <a href="/ask-advisor" className="btn btn-gradient btn-lg">
                🤖 Ask Our AI Advisor
              </a>
            </div>
          </>
        )}
      </div>
    </div>
  );
};

export default InvestmentsPage;