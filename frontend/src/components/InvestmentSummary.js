import React from 'react';

const InvestmentSummary = ({ summary }) => {
  const getRecommendationColor = (type) => {
    const colors = {
      'BUY': 'text-green-400',
      'HOLD': 'text-yellow-400', 
      'SELL': 'text-red-400'
    };
    return colors[type] || 'text-gray-400';
  };

  const getAssetTypeIcon = (type) => {
    const icons = {
      'stocks': '📈',
      'indices': '📊',
      'commodities': '🏅'
    };
    return icons[type] || '💼';
  };

  return (
    <div className="mb-8">
      <h2 className="text-2xl font-semibold mb-6">Market Overview</h2>
      
      {/* Summary Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
        {/* Total Recommendations */}
        <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-gray-400 text-sm">Total Recommendations</p>
              <p className="text-2xl font-bold text-white">{summary.total_recommendations}</p>
            </div>
            <div className="text-2xl">💡</div>
          </div>
        </div>

        {/* Buy Recommendations */}
        <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-gray-400 text-sm">Buy Signals</p>
              <p className="text-2xl font-bold text-green-400">{summary.recommendations_by_type.BUY}</p>
            </div>
            <div className="text-2xl">📈</div>
          </div>
        </div>

        {/* Hold Recommendations */}
        <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-gray-400 text-sm">Hold Positions</p>
              <p className="text-2xl font-bold text-yellow-400">{summary.recommendations_by_type.HOLD}</p>
            </div>
            <div className="text-2xl">⏸️</div>
          </div>
        </div>

        {/* Sell Recommendations */}
        <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-gray-400 text-sm">Sell Signals</p>
              <p className="text-2xl font-bold text-red-400">{summary.recommendations_by_type.SELL}</p>
            </div>
            <div className="text-2xl">📉</div>
          </div>
        </div>
      </div>

      {/* Asset Breakdown */}
      <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
        <h3 className="text-lg font-semibold mb-4">Asset Distribution</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="flex items-center justify-between p-4 bg-gray-700 rounded-lg">
            <div className="flex items-center space-x-3">
              <span className="text-xl">{getAssetTypeIcon('stocks')}</span>
              <span className="text-white font-medium">Stocks</span>
            </div>
            <span className="text-blue-400 font-bold">{summary.assets_by_type.stocks}</span>
          </div>
          
          <div className="flex items-center justify-between p-4 bg-gray-700 rounded-lg">
            <div className="flex items-center space-x-3">
              <span className="text-xl">{getAssetTypeIcon('indices')}</span>
              <span className="text-white font-medium">Indices</span>
            </div>
            <span className="text-purple-400 font-bold">{summary.assets_by_type.indices}</span>
          </div>
          
          <div className="flex items-center justify-between p-4 bg-gray-700 rounded-lg">
            <div className="flex items-center space-x-3">
              <span className="text-xl">{getAssetTypeIcon('commodities')}</span>
              <span className="text-white font-medium">Commodities</span>
            </div>
            <span className="text-yellow-400 font-bold">{summary.assets_by_type.commodities}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default InvestmentSummary;