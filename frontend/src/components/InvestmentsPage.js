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

  const getAssetTypeDisplayName = (assetType) => {
    const names = {
      'stock': 'Stocks',
      'index': 'Indices',
      'commodity': 'Commodities'
    };
    return names[assetType] || assetType;
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-4xl font-bold mb-4">Investment Recommendations</h1>
          <p className="text-gray-400 text-lg">Expert analysis and predictions for stocks, indices, and commodities</p>
        </div>

        {/* Summary Dashboard */}
        {summary && <InvestmentSummary summary={summary} />}

        {/* Asset Type Filter */}
        <div className="mb-8">
          <h3 className="text-lg font-semibold mb-4">Filter by Asset Type</h3>
          <div className="flex flex-wrap gap-2">
            <button
              onClick={() => handleAssetTypeChange('')}
              className={`px-4 py-2 rounded-full text-sm font-medium transition-colors duration-200 ${
                selectedAssetType === ''
                  ? 'bg-blue-600 text-white'
                  : 'bg-gray-800 text-gray-300 hover:bg-gray-700'
              }`}
            >
              All ({summary?.total_recommendations || 0})
            </button>
            {assetTypes.map((type) => (
              <button
                key={type.asset_type}
                onClick={() => handleAssetTypeChange(type.asset_type)}
                className={`px-4 py-2 rounded-full text-sm font-medium transition-colors duration-200 ${
                  selectedAssetType === type.asset_type
                    ? 'bg-blue-600 text-white'
                    : 'bg-gray-800 text-gray-300 hover:bg-gray-700'
                }`}
              >
                {getAssetTypeDisplayName(type.asset_type)} ({type.count})
              </button>
            ))}
          </div>
        </div>

        {/* Content */}
        {loading ? (
          <div className="flex justify-center items-center py-12">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
          </div>
        ) : error ? (
          <div className="text-center py-12">
            <div className="text-red-400 mb-4">{error}</div>
            <button
              onClick={fetchRecommendations}
              className="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-md transition-colors duration-200"
            >
              Try Again
            </button>
          </div>
        ) : recommendations.length === 0 ? (
          <div className="text-center py-12">
            <div className="text-gray-400 mb-4">No recommendations found for the selected asset type.</div>
            <button
              onClick={() => handleAssetTypeChange('')}
              className="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-md transition-colors duration-200"
            >
              View All Recommendations
            </button>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {recommendations.map((recommendation) => (
              <InvestmentCard key={recommendation.id} recommendation={recommendation} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default InvestmentsPage;