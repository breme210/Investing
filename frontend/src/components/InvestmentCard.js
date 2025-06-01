import React from 'react';
import { Link } from 'react-router-dom';

const InvestmentCard = ({ recommendation }) => {
  const formatPrice = (price) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    }).format(price);
  };

  const formatChange = (change, isPercent = false) => {
    const value = isPercent ? `${change.toFixed(2)}%` : formatPrice(Math.abs(change));
    return change >= 0 ? `+${value}` : `-${value}`;
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
    const change = ((recommendation.target_price - recommendation.current_price) / recommendation.current_price) * 100;
    return change;
  };

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  return (
    <Link to={`/investments/${recommendation.id}`} className="block group">
      <div className="bg-gray-800 rounded-lg p-6 border border-gray-700 hover:border-gray-600 transition-all duration-300 transform hover:scale-105">
        {/* Header */}
        <div className="flex items-start justify-between mb-4">
          <div className="flex items-center space-x-2">
            <span className="text-xl">{getAssetTypeIcon(recommendation.asset_type)}</span>
            <div>
              <h3 className="text-lg font-bold text-white group-hover:text-blue-400 transition-colors">
                {recommendation.symbol}
              </h3>
              <p className="text-sm text-gray-400">{recommendation.name}</p>
            </div>
          </div>
          <span className={`px-2 py-1 rounded text-xs font-medium ${getRecommendationColor(recommendation.recommendation)}`}>
            {recommendation.recommendation}
          </span>
        </div>

        {/* Price Information */}
        <div className="mb-4">
          <div className="flex items-center justify-between mb-2">
            <span className="text-sm text-gray-400">Current Price</span>
            <span className="text-lg font-semibold text-white">
              {recommendation.symbol === 'BTC-USD' ? 
                `$${recommendation.current_price.toLocaleString()}` : 
                formatPrice(recommendation.current_price)
              }
            </span>
          </div>
          
          <div className="flex items-center justify-between mb-2">
            <span className="text-sm text-gray-400">Target Price</span>
            <span className="text-lg font-semibold text-blue-400">
              {recommendation.symbol === 'BTC-USD' ? 
                `$${recommendation.target_price.toLocaleString()}` : 
                formatPrice(recommendation.target_price)
              }
            </span>
          </div>

          <div className="flex items-center justify-between">
            <span className="text-sm text-gray-400">24h Change</span>
            <span className={`text-sm font-medium ${getPriceChangeColor(recommendation.price_change_24h)}`}>
              {formatChange(recommendation.price_change_percent, true)}
            </span>
          </div>
        </div>

        {/* Target Upside */}
        <div className="mb-4 p-3 bg-gray-700 rounded-lg">
          <div className="flex items-center justify-between">
            <span className="text-sm text-gray-400">Potential Upside</span>
            <span className={`text-lg font-bold ${getTargetPriceChange() >= 0 ? 'text-green-400' : 'text-red-400'}`}>
              {getTargetPriceChange() >= 0 ? '+' : ''}{getTargetPriceChange().toFixed(1)}%
            </span>
          </div>
        </div>

        {/* Risk and Confidence */}
        <div className="flex items-center justify-between mb-4">
          <div>
            <span className="text-xs text-gray-400">Risk Level</span>
            <p className={`text-sm font-medium ${getRiskColor(recommendation.risk_level)}`}>
              {recommendation.risk_level}
            </p>
          </div>
          <div className="text-right">
            <span className="text-xs text-gray-400">Confidence</span>
            <p className="text-sm font-medium text-white">{recommendation.confidence_score}%</p>
          </div>
          <div className="text-right">
            <span className="text-xs text-gray-400">Timeframe</span>
            <p className="text-sm font-medium text-white">{recommendation.timeframe}</p>
          </div>
        </div>

        {/* Additional Info */}
        <div className="flex items-center justify-between text-xs text-gray-500">
          <span>By {recommendation.analyst}</span>
          <span>{formatDate(recommendation.last_updated)}</span>
        </div>

        {/* Market Cap (for stocks) */}
        {recommendation.market_cap && (
          <div className="mt-2 pt-2 border-t border-gray-700">
            <div className="flex items-center justify-between text-xs">
              <span className="text-gray-400">Market Cap</span>
              <span className="text-gray-300">{recommendation.market_cap}</span>
            </div>
          </div>
        )}
      </div>
    </Link>
  );
};

export default InvestmentCard;