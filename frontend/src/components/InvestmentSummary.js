import React from 'react';

const InvestmentSummary = ({ summary }) => {
  const getRecommendationConfig = (type, value) => {
    const configs = {
      'BUY': { 
        color: 'text-green-400', 
        bgColor: 'bg-green-400/10', 
        icon: '🚀',
        percentage: summary.total_recommendations > 0 ? ((value / summary.total_recommendations) * 100).toFixed(0) : 0
      },
      'HOLD': { 
        color: 'text-yellow-400', 
        bgColor: 'bg-yellow-400/10', 
        icon: '⏸️',
        percentage: summary.total_recommendations > 0 ? ((value / summary.total_recommendations) * 100).toFixed(0) : 0
      },
      'SELL': { 
        color: 'text-red-400', 
        bgColor: 'bg-red-400/10', 
        icon: '📉',
        percentage: summary.total_recommendations > 0 ? ((value / summary.total_recommendations) * 100).toFixed(0) : 0
      }
    };
    return configs[type] || configs['HOLD'];
  };

  const getAssetTypeConfig = (type) => {
    const configs = {
      'stocks': { icon: '📈', color: 'text-blue-400', label: 'Stocks' },
      'indices': { icon: '📊', color: 'text-purple-400', label: 'Indices' },
      'commodities': { icon: '🏅', color: 'text-orange-400', label: 'Commodities' }
    };
    return configs[type] || { icon: '💼', color: 'text-gray-400', label: type };
  };

  const totalRecommendations = summary.total_recommendations || 0;
  const buyCount = summary.recommendations_by_type?.BUY || 0;
  const holdCount = summary.recommendations_by_type?.HOLD || 0;
  const sellCount = summary.recommendations_by_type?.SELL || 0;

  // Calculate market sentiment
  const getMarketSentiment = () => {
    if (totalRecommendations === 0) return { label: 'Neutral', color: 'text-gray-400', icon: '➖' };
    const buyPercentage = (buyCount / totalRecommendations) * 100;
    
    if (buyPercentage >= 60) return { label: 'Bullish', color: 'text-green-400', icon: '📈' };
    if (buyPercentage >= 40) return { label: 'Neutral', color: 'text-yellow-400', icon: '➖' };
    return { label: 'Bearish', color: 'text-red-400', icon: '📉' };
  };

  const sentiment = getMarketSentiment();

  return (
    <div className="mb-12">
      <div className="text-center mb-8">
        <h2 className="heading-2 mb-4">Market Intelligence Dashboard</h2>
        <p className="text-gray-400">Real-time overview of our investment recommendations and market sentiment</p>
      </div>
      
      {/* Market Sentiment Header */}
      <div className="text-center mb-8">
        <div className="inline-flex items-center space-x-3 bg-gray-800 px-6 py-3 rounded-2xl border border-gray-700">
          <span className="text-2xl">{sentiment.icon}</span>
          <div>
            <span className="text-gray-400 text-sm">Market Sentiment: </span>
            <span className={`font-bold text-lg ${sentiment.color}`}>{sentiment.label}</span>
          </div>
        </div>
      </div>

      {/* Summary Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        {/* Total Recommendations */}
        <div className="card bg-gradient-to-br from-blue-600/20 to-purple-600/20 border-blue-500/30">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-gray-300 text-sm font-medium mb-1">Total Recommendations</p>
              <p className="text-3xl font-bold text-white">{totalRecommendations}</p>
              <p className="text-xs text-gray-400 mt-1">Active Positions</p>
            </div>
            <div className="w-12 h-12 bg-blue-500/20 rounded-xl flex items-center justify-center">
              <span className="text-2xl">💡</span>
            </div>
          </div>
        </div>

        {/* Buy Recommendations */}
        {(() => {
          const config = getRecommendationConfig('BUY', buyCount);
          return (
            <div className={`card ${config.bgColor} border-green-500/30`}>
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-gray-300 text-sm font-medium mb-1">Buy Signals</p>
                  <p className={`text-3xl font-bold ${config.color}`}>{buyCount}</p>
                  <p className="text-xs text-gray-400 mt-1">{config.percentage}% of total</p>
                </div>
                <div className="w-12 h-12 bg-green-500/20 rounded-xl flex items-center justify-center">
                  <span className="text-2xl">{config.icon}</span>
                </div>
              </div>
              
              {/* Progress bar */}
              <div className="mt-4">
                <div className="w-full bg-gray-700 rounded-full h-2">
                  <div 
                    className="bg-green-500 h-2 rounded-full transition-all duration-500"
                    style={{ width: `${config.percentage}%` }}
                  ></div>
                </div>
              </div>
            </div>
          );
        })()}

        {/* Hold Recommendations */}
        {(() => {
          const config = getRecommendationConfig('HOLD', holdCount);
          return (
            <div className={`card ${config.bgColor} border-yellow-500/30`}>
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-gray-300 text-sm font-medium mb-1">Hold Positions</p>
                  <p className={`text-3xl font-bold ${config.color}`}>{holdCount}</p>
                  <p className="text-xs text-gray-400 mt-1">{config.percentage}% of total</p>
                </div>
                <div className="w-12 h-12 bg-yellow-500/20 rounded-xl flex items-center justify-center">
                  <span className="text-2xl">{config.icon}</span>
                </div>
              </div>
              
              {/* Progress bar */}
              <div className="mt-4">
                <div className="w-full bg-gray-700 rounded-full h-2">
                  <div 
                    className="bg-yellow-500 h-2 rounded-full transition-all duration-500"
                    style={{ width: `${config.percentage}%` }}
                  ></div>
                </div>
              </div>
            </div>
          );
        })()}

        {/* Sell Recommendations */}
        {(() => {
          const config = getRecommendationConfig('SELL', sellCount);
          return (
            <div className={`card ${config.bgColor} border-red-500/30`}>
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-gray-300 text-sm font-medium mb-1">Sell Signals</p>
                  <p className={`text-3xl font-bold ${config.color}`}>{sellCount}</p>
                  <p className="text-xs text-gray-400 mt-1">{config.percentage}% of total</p>
                </div>
                <div className="w-12 h-12 bg-red-500/20 rounded-xl flex items-center justify-center">
                  <span className="text-2xl">{config.icon}</span>
                </div>
              </div>
              
              {/* Progress bar */}
              <div className="mt-4">
                <div className="w-full bg-gray-700 rounded-full h-2">
                  <div 
                    className="bg-red-500 h-2 rounded-full transition-all duration-500"
                    style={{ width: `${config.percentage}%` }}
                  ></div>
                </div>
              </div>
            </div>
          );
        })()}
      </div>

      {/* Asset Distribution */}
      <div className="card">
        <div className="flex items-center mb-6">
          <span className="text-2xl mr-3">🎯</span>
          <h3 className="text-xl font-semibold text-white">Asset Distribution</h3>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {Object.entries(summary.assets_by_type || {}).map(([type, count]) => {
            const config = getAssetTypeConfig(type);
            const percentage = totalRecommendations > 0 ? ((count / totalRecommendations) * 100).toFixed(0) : 0;
            
            return (
              <div key={type} className="bg-gray-700/50 rounded-xl p-4 hover:bg-gray-700/70 transition-colors">
                <div className="flex items-center justify-between mb-3">
                  <div className="flex items-center space-x-3">
                    <div className={`w-10 h-10 rounded-lg ${config.color} bg-opacity-20 flex items-center justify-center`}>
                      <span className="text-lg">{config.icon}</span>
                    </div>
                    <span className="text-white font-medium">{config.label}</span>
                  </div>
                  <div className="text-right">
                    <span className={`text-xl font-bold ${config.color}`}>{count}</span>
                    <div className="text-xs text-gray-400">{percentage}%</div>
                  </div>
                </div>
                
                {/* Progress bar */}
                <div className="w-full bg-gray-600 rounded-full h-2">
                  <div 
                    className={`h-2 rounded-full transition-all duration-500 ${config.color.replace('text-', 'bg-')}`}
                    style={{ width: `${percentage}%` }}
                  ></div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

export default InvestmentSummary;