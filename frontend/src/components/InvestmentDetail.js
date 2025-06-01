import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';

const InvestmentDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [recommendation, setRecommendation] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const backendUrl = process.env.REACT_APP_BACKEND_URL || import.meta.env.REACT_APP_BACKEND_URL;

  useEffect(() => {
    fetchRecommendation();
  }, [id]);

  const fetchRecommendation = async () => {
    try {
      setLoading(true);
      const response = await fetch(`${backendUrl}/api/investments/${id}`);
      
      if (!response.ok) {
        if (response.status === 404) {
          setError('Investment recommendation not found');
        } else {
          throw new Error('Failed to fetch recommendation');
        }
        return;
      }
      
      const data = await response.json();
      setRecommendation(data);
      setError(null);
    } catch (err) {
      setError('Failed to load recommendation. Please try again later.');
      console.error('Error fetching recommendation:', err);
    } finally {
      setLoading(false);
    }
  };

  const formatPrice = (price) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    }).format(price);
  };

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const getRecommendationColor = (rec) => {
    const colors = {
      'BUY': 'bg-green-600 text-white',
      'HOLD': 'bg-yellow-600 text-white',
      'SELL': 'bg-red-600 text-white'
    };
    return colors[rec] || 'bg-gray-600 text-white';
  };

  const getRiskColor = (risk) => {
    const colors = {
      'LOW': 'text-green-400',
      'MEDIUM': 'text-yellow-400',
      'HIGH': 'text-red-400'
    };
    return colors[risk] || 'text-gray-400';
  };

  const getAssetTypeIcon = (type) => {
    const icons = {
      'stock': '📈',
      'index': '📊',
      'commodity': '🏅'
    };
    return icons[type] || '💼';
  };

  const getPriceChangeColor = (change) => {
    return change >= 0 ? 'text-green-400' : 'text-red-400';
  };

  const getTargetPriceChange = () => {
    if (!recommendation) return 0;
    const change = ((recommendation.target_price - recommendation.current_price) / recommendation.current_price) * 100;
    return change;
  };

  const getAssetTypeDisplayName = (type) => {
    const names = {
      'stock': 'Stock',
      'index': 'Index',
      'commodity': 'Commodity'
    };
    return names[type] || type;
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-900 text-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="flex justify-center items-center py-12">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gray-900 text-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="text-center py-12">
            <div className="text-red-400 mb-4 text-lg">{error}</div>
            <div className="space-x-4">
              <button
                onClick={fetchRecommendation}
                className="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-md transition-colors duration-200"
              >
                Try Again
              </button>
              <Link
                to="/investments"
                className="bg-gray-600 hover:bg-gray-700 px-4 py-2 rounded-md transition-colors duration-200 inline-block"
              >
                Back to Investments
              </Link>
            </div>
          </div>
        </div>
      </div>
    );
  }

  if (!recommendation) {
    return null;
  }

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Back Button */}
        <button
          onClick={() => navigate(-1)}
          className="flex items-center text-gray-400 hover:text-white mb-6 transition-colors duration-200"
        >
          <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
          </svg>
          Back to Investments
        </button>

        {/* Header */}
        <div className="bg-gray-800 rounded-lg p-6 mb-8 border border-gray-700">
          <div className="flex items-start justify-between mb-4">
            <div className="flex items-center space-x-3">
              <span className="text-3xl">{getAssetTypeIcon(recommendation.asset_type)}</span>
              <div>
                <h1 className="text-3xl font-bold text-white">{recommendation.symbol}</h1>
                <p className="text-lg text-gray-400">{recommendation.name}</p>
                <p className="text-sm text-gray-500">{getAssetTypeDisplayName(recommendation.asset_type)}</p>
              </div>
            </div>
            <span className={`px-4 py-2 rounded-lg text-lg font-bold ${getRecommendationColor(recommendation.recommendation)}`}>
              {recommendation.recommendation}
            </span>
          </div>

          {/* Key Metrics */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="text-center p-4 bg-gray-700 rounded-lg">
              <p className="text-sm text-gray-400 mb-1">Current Price</p>
              <p className="text-2xl font-bold text-white">
                {recommendation.symbol === 'BTC-USD' ? 
                  `$${recommendation.current_price.toLocaleString()}` : 
                  formatPrice(recommendation.current_price)
                }
              </p>
              <p className={`text-sm ${getPriceChangeColor(recommendation.price_change_24h)}`}>
                {recommendation.price_change_24h >= 0 ? '+' : ''}{recommendation.price_change_percent.toFixed(2)}% (24h)
              </p>
            </div>

            <div className="text-center p-4 bg-gray-700 rounded-lg">
              <p className="text-sm text-gray-400 mb-1">Target Price</p>
              <p className="text-2xl font-bold text-blue-400">
                {recommendation.symbol === 'BTC-USD' ? 
                  `$${recommendation.target_price.toLocaleString()}` : 
                  formatPrice(recommendation.target_price)
                }
              </p>
              <p className="text-sm text-gray-400">{recommendation.timeframe} target</p>
            </div>

            <div className="text-center p-4 bg-gray-700 rounded-lg">
              <p className="text-sm text-gray-400 mb-1">Potential Upside</p>
              <p className={`text-2xl font-bold ${getTargetPriceChange() >= 0 ? 'text-green-400' : 'text-red-400'}`}>
                {getTargetPriceChange() >= 0 ? '+' : ''}{getTargetPriceChange().toFixed(1)}%
              </p>
              <p className="text-sm text-gray-400">To target</p>
            </div>
          </div>
        </div>

        {/* Analysis Section */}
        <div className="bg-gray-800 rounded-lg p-6 mb-8 border border-gray-700">
          <h2 className="text-xl font-semibold mb-4">Investment Analysis</h2>
          <div className="prose prose-lg prose-invert max-w-none">
            <p className="text-gray-300 leading-relaxed text-lg whitespace-pre-line">
              {recommendation.analysis}
            </p>
          </div>
        </div>

        {/* Key Factors */}
        <div className="bg-gray-800 rounded-lg p-6 mb-8 border border-gray-700">
          <h2 className="text-xl font-semibold mb-4">Key Investment Factors</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {recommendation.key_factors.map((factor, index) => (
              <div key={index} className="flex items-start space-x-3 p-3 bg-gray-700 rounded-lg">
                <div className="flex-shrink-0 w-2 h-2 bg-blue-500 rounded-full mt-2"></div>
                <p className="text-gray-300">{factor}</p>
              </div>
            ))}
          </div>
        </div>

        {/* Risk and Confidence Metrics */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
          <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
            <h3 className="text-lg font-semibold mb-4">Risk Assessment</h3>
            <div className="flex items-center justify-between mb-3">
              <span className="text-gray-400">Risk Level</span>
              <span className={`text-lg font-bold ${getRiskColor(recommendation.risk_level)}`}>
                {recommendation.risk_level}
              </span>
            </div>
            <div className="flex items-center justify-between mb-3">
              <span className="text-gray-400">Confidence Score</span>
              <span className="text-lg font-bold text-white">{recommendation.confidence_score}%</span>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-gray-400">Time Horizon</span>
              <span className="text-lg font-bold text-white">{recommendation.timeframe}</span>
            </div>
          </div>

          {/* Additional Info */}
          <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
            <h3 className="text-lg font-semibold mb-4">Additional Information</h3>
            {recommendation.market_cap && (
              <div className="flex items-center justify-between mb-3">
                <span className="text-gray-400">Market Cap</span>
                <span className="text-white font-medium">{recommendation.market_cap}</span>
              </div>
            )}
            {recommendation.sector && (
              <div className="flex items-center justify-between mb-3">
                <span className="text-gray-400">Sector</span>
                <span className="text-white font-medium">{recommendation.sector}</span>
              </div>
            )}
            <div className="flex items-center justify-between mb-3">
              <span className="text-gray-400">Analyst</span>
              <span className="text-white font-medium">{recommendation.analyst}</span>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-gray-400">Last Updated</span>
              <span className="text-white font-medium">{formatDate(recommendation.last_updated)}</span>
            </div>
          </div>
        </div>

        {/* Navigation */}
        <div className="border-t border-gray-800 pt-8">
          <div className="flex justify-between items-center">
            <Link
              to="/investments"
              className="bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded-md transition-colors duration-200 font-medium"
            >
              View All Recommendations
            </Link>
            <Link
              to={`/investments?asset_type=${recommendation.asset_type}`}
              className="text-gray-400 hover:text-white transition-colors duration-200"
            >
              More {getAssetTypeDisplayName(recommendation.asset_type)} Recommendations
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default InvestmentDetail;