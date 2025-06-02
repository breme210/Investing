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
    const value = isPercent ? `${Math.abs(change).toFixed(2)}%` : formatPrice(Math.abs(change));
    return change >= 0 ? `+${value}` : `-${value}`;
  };

  const getRecommendationConfig = (rec) => {
    const configs = {
      'BUY': { 
        color: 'bg-gradient-to-r from-green-500 to-green-600', 
        icon: '🚀', 
        textColor: 'text-white',
        description: 'Strong Buy Signal'
      },
      'HOLD': { 
        color: 'bg-gradient-to-r from-yellow-500 to-yellow-600', 
        icon: '⏸️', 
        textColor: 'text-white',
        description: 'Hold Position'
      },
      'SELL': { 
        color: 'bg-gradient-to-r from-red-500 to-red-600', 
        icon: '📉', 
        textColor: 'text-white',
        description: 'Consider Selling'
      }
    };
    return configs[rec] || configs['HOLD'];
  };

  const getRiskConfig = (risk) => {
    const configs = {
      'LOW': { color: 'text-green-400', bg: 'bg-green-400/10', icon: '🛡️', description: 'Conservative' },
      'MEDIUM': { color: 'text-yellow-400', bg: 'bg-yellow-400/10', icon: '⚖️', description: 'Moderate' },
      'HIGH': { color: 'text-red-400', bg: 'bg-red-400/10', icon: '⚡', description: 'Aggressive' }
    };
    return configs[risk] || configs['MEDIUM'];
  };

  const getAssetTypeConfig = (type) => {
    const configs = {
      'stock': { icon: '📈', label: 'Stock', color: 'text-blue-400' },
      'index': { icon: '📊', label: 'Index', color: 'text-purple-400' },
      'commodity': { icon: '🏅', label: 'Commodity', color: 'text-orange-400' }
    };
    return configs[type] || { icon: '💼', label: 'Asset', color: 'text-gray-400' };
  };

  const getPriceChangeColor = (change) => {
    return change >= 0 ? 'text-green-400' : 'text-red-400';
  };

  const getTargetPriceChange = () => {
    const change = ((recommendation.target_price - recommendation.current_price) / recommendation.current_price) * 100;
    return change;
  };

  const getConfidenceColor = (confidence) => {
    if (confidence >= 80) return 'text-green-400';
    if (confidence >= 60) return 'text-yellow-400';
    return 'text-red-400';
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

  const recConfig = getRecommendationConfig(recommendation.recommendation);
  const riskConfig = getRiskConfig(recommendation.risk_level);
  const assetConfig = getAssetTypeConfig(recommendation.asset_type);
  const targetChange = getTargetPriceChange();

  return (
    <Link to={`/investments/${recommendation.id}`} className="block group">
      <div className="card group-hover:scale-105 group-hover:border-blue-500/50 transition-all duration-300">
        {/* Header with Asset Type and Recommendation */}
        <div className="flex items-start justify-between mb-6">
          <div className="flex items-center space-x-3">
            <div className={`w-12 h-12 rounded-xl ${assetConfig.color} bg-opacity-20 flex items-center justify-center`}>
              <span className="text-xl">{assetConfig.icon}</span>
            </div>
            <div>
              <h3 className="text-xl font-bold text-white group-hover:text-blue-400 transition-colors">
                {recommendation.symbol}
              </h3>
              <p className="text-sm text-gray-400">{recommendation.name}</p>
              <span className={`text-xs font-medium ${assetConfig.color}`}>
                {assetConfig.label}
              </span>
            </div>
          </div>
          
          <div className={`${recConfig.color} ${recConfig.textColor} px-3 py-2 rounded-xl text-sm font-bold shadow-lg flex items-center space-x-1`}>
            <span>{recConfig.icon}</span>
            <span>{recommendation.recommendation}</span>
          </div>
        </div>

        {/* Price Section */}
        <div className="space-y-4 mb-6">
          {/* Current Price */}
          <div className="flex items-center justify-between">
            <span className="text-gray-400 font-medium">Current Price</span>
            <div className="text-right">
              <span className="text-2xl font-bold text-white">
                {recommendation.symbol === 'BTC-USD' ? 
                  `$${recommendation.current_price.toLocaleString()}` : 
                  formatPrice(recommendation.current_price)
                }
              </span>
              <div className={`text-sm font-medium ${getPriceChangeColor(recommendation.price_change_24h)}`}>
                {formatChange(recommendation.price_change_percent, true)} (24h)
              </div>
            </div>
          </div>
          
          {/* Target Price */}
          <div className="flex items-center justify-between">
            <span className="text-gray-400 font-medium">Target Price</span>
            <span className="text-xl font-bold text-blue-400">
              {recommendation.symbol === 'BTC-USD' ? 
                `$${recommendation.target_price.toLocaleString()}` : 
                formatPrice(recommendation.target_price)
              }
            </span>
          </div>
        </div>

        {/* Potential Upside - Highlighted Section */}
        <div className={`p-4 rounded-xl mb-6 ${targetChange >= 0 ? 'bg-green-500/10 border border-green-500/20' : 'bg-red-500/10 border border-red-500/20'}`}>
          <div className="flex items-center justify-between">
            <div>
              <span className="text-gray-400 text-sm font-medium">Potential Return</span>
              <div className="text-xs text-gray-500">{recommendation.timeframe}</div>
            </div>
            <div className="text-right">
              <span className={`text-2xl font-bold ${targetChange >= 0 ? 'text-green-400' : 'text-red-400'}`}>
                {targetChange >= 0 ? '+' : ''}{targetChange.toFixed(1)}%
              </span>
            </div>
          </div>
          
          {/* Progress bar showing target progress */}
          <div className="mt-3">
            <div className="w-full bg-gray-700 rounded-full h-2">
              <div 
                className={`h-2 rounded-full transition-all duration-500 ${targetChange >= 0 ? 'bg-green-500' : 'bg-red-500'}`}
                style={{ width: `${Math.min(Math.abs(targetChange), 100)}%` }}
              ></div>
            </div>
          </div>
        </div>

        {/* Risk and Confidence Grid */}
        <div className="grid grid-cols-2 gap-4 mb-6">
          {/* Risk Level */}
          <div className={`${riskConfig.bg} rounded-xl p-3`}>
            <div className="flex items-center space-x-2 mb-1">
              <span>{riskConfig.icon}</span>
              <span className="text-xs text-gray-400">Risk Level</span>
            </div>
            <div className={`font-bold ${riskConfig.color}`}>
              {recommendation.risk_level}
            </div>
            <div className="text-xs text-gray-500">{riskConfig.description}</div>
          </div>
          
          {/* Confidence Score */}
          <div className="bg-gray-700/50 rounded-xl p-3">
            <div className="flex items-center space-x-2 mb-1">
              <span>🎯</span>
              <span className="text-xs text-gray-400">Confidence</span>
            </div>
            <div className={`font-bold ${getConfidenceColor(recommendation.confidence_score)}`}>
              {recommendation.confidence_score}%
            </div>
            <div className="text-xs text-gray-500">Analyst Rating</div>
          </div>
        </div>

        {/* Technical Indicators (if available) */}
        {recommendation.technical_indicators && (
          <div className="mb-6 p-4 bg-gray-700/30 rounded-xl">
            <h4 className="text-sm font-medium text-gray-300 mb-3 flex items-center">
              <span className="mr-2">📊</span>
              Technical Indicators
            </h4>
            <div className="grid grid-cols-2 gap-3 text-xs">
              {recommendation.technical_indicators.rsi && (
                <div>
                  <span className="text-gray-400">RSI:</span>
                  <span className={`ml-1 font-medium ${
                    recommendation.technical_indicators.rsi > 70 ? 'text-red-400' : 
                    recommendation.technical_indicators.rsi < 30 ? 'text-green-400' : 'text-gray-300'
                  }`}>
                    {recommendation.technical_indicators.rsi.toFixed(1)}
                  </span>
                </div>
              )}
              {recommendation.technical_indicators.pe_ratio && (
                <div>
                  <span className="text-gray-400">P/E:</span>
                  <span className="ml-1 font-medium text-gray-300">
                    {recommendation.technical_indicators.pe_ratio.toFixed(1)}
                  </span>
                </div>
              )}
            </div>
          </div>
        )}

        {/* Footer Information */}
        <div className="flex items-center justify-between text-xs text-gray-500 pt-4 border-t border-gray-700">
          <div className="flex items-center space-x-1">
            <span>👨‍💼</span>
            <span>{recommendation.analyst}</span>
          </div>
          <div className="flex items-center space-x-1">
            <span>🕒</span>
            <span>{formatDate(recommendation.last_updated)}</span>
          </div>
        </div>

        {/* Market Cap (for stocks) */}
        {recommendation.market_cap && (
          <div className="mt-3 flex items-center justify-between text-xs">
            <span className="text-gray-400">Market Cap:</span>
            <span className="text-gray-300 font-medium">{recommendation.market_cap}</span>
          </div>
        )}

        {/* Sector (if available) */}
        {recommendation.sector && (
          <div className="mt-2 flex items-center justify-between text-xs">
            <span className="text-gray-400">Sector:</span>
            <span className="text-gray-300 font-medium">{recommendation.sector}</span>
          </div>
        )}
      </div>
    </Link>
  );
};

export default InvestmentCard;