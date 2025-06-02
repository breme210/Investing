import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import '../styles/DesignSystem.css';

const HomePage = () => {
  const [status, setStatus] = useState('');
  const [loading, setLoading] = useState(true);
  const [stats, setStats] = useState({
    totalRecommendations: 0,
    buyRecommendations: 0,
    averageConfidence: 0
  });

  useEffect(() => {
    const fetchData = async () => {
      try {
        const backendUrl = process.env.REACT_APP_BACKEND_URL || import.meta.env.REACT_APP_BACKEND_URL;
        
        // Fetch basic status
        const statusResponse = await fetch(`${backendUrl}/api/`);
        const statusData = await statusResponse.json();
        setStatus(statusData.message);

        // Fetch investment summary for stats
        const summaryResponse = await fetch(`${backendUrl}/api/investments/summary`);
        const summaryData = await summaryResponse.json();
        
        setStats({
          totalRecommendations: summaryData.total_recommendations,
          buyRecommendations: summaryData.recommendations_by_type?.BUY || 0,
          averageConfidence: 85 // Mock data for now
        });
        
      } catch (error) {
        console.error('Error fetching data:', error);
        setStatus('Error connecting to backend');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const features = [
    {
      icon: '🤖',
      title: 'AI-Powered Analysis',
      description: 'Get intelligent investment recommendations powered by advanced algorithms and real-time market data.',
      link: '/ask-advisor'
    },
    {
      icon: '📊',
      title: 'Investment Insights',
      description: 'Discover comprehensive analysis on stocks, indices, and commodities with detailed risk assessments.',
      link: '/investments'
    },
    {
      icon: '📰',
      title: 'Market News',
      description: 'Stay informed with curated financial news and market updates from trusted sources.',
      link: '/news'
    }
  ];

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-900 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mx-auto mb-4"></div>
          <p className="text-gray-400">Loading your financial dashboard...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      {/* Hero Section */}
      <section className="relative overflow-hidden">
        {/* Background Image with Overlay */}
        <div className="absolute inset-0">
          <img 
            src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab"
            alt="Financial District"
            className="w-full h-full object-cover"
          />
          <div className="absolute inset-0 bg-gradient-to-r from-gray-900/95 via-gray-900/80 to-gray-900/95"></div>
        </div>
        
        {/* Hero Content */}
        <div className="relative container-fluid py-24 lg:py-32">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div className="animate-fade-in-up">
              <h1 className="heading-1 mb-6">
                Smart <span className="text-gradient">Investment</span> Decisions 
                <br />Start Here
              </h1>
              <p className="text-xl text-secondary mb-8 leading-relaxed">
                Harness the power of AI-driven analysis to make informed investment decisions. 
                Get personalized recommendations, market insights, and real-time advisory support.
              </p>
              
              {/* CTA Buttons */}
              <div className="flex flex-col sm:flex-row gap-4 mb-8">
                <Link to="/ask-advisor" className="btn btn-gradient btn-lg">
                  🚀 Start with AI Advisor
                </Link>
                <Link to="/investments" className="btn btn-outline btn-lg">
                  📊 View Recommendations
                </Link>
              </div>

              {/* Status Indicator */}
              {status && (
                <div className="flex items-center space-x-2">
                  <div className="w-3 h-3 bg-green-500 rounded-full animate-pulse"></div>
                  <span className="text-green-400 text-sm font-medium">System Status: {status}</span>
                </div>
              )}
            </div>
            
            {/* Stats Dashboard */}
            <div className="animate-fade-in-scale">
              <div className="card card-premium p-8">
                <h3 className="heading-3 mb-6 text-center">Live Market Intelligence</h3>
                <div className="grid grid-cols-3 gap-6">
                  <div className="text-center">
                    <div className="text-3xl font-bold text-blue-400 mb-2">{stats.totalRecommendations}</div>
                    <div className="text-sm text-muted">Active Recommendations</div>
                  </div>
                  <div className="text-center">
                    <div className="text-3xl font-bold text-green-400 mb-2">{stats.buyRecommendations}</div>
                    <div className="text-sm text-muted">Buy Signals</div>
                  </div>
                  <div className="text-center">
                    <div className="text-3xl font-bold text-purple-400 mb-2">{stats.averageConfidence}%</div>
                    <div className="text-sm text-muted">Avg Confidence</div>
                  </div>
                </div>
                
                {/* Quick Action */}
                <div className="mt-6 pt-6 border-t border-gray-700">
                  <Link to="/ask-advisor" className="btn btn-primary w-full">
                    Ask Our AI Advisor
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 bg-gradient-to-b from-gray-900 to-gray-800">
        <div className="container">
          <div className="text-center mb-16">
            <h2 className="heading-2 mb-6">Everything You Need for Smart Investing</h2>
            <p className="text-xl text-secondary max-w-3xl mx-auto">
              Our comprehensive platform combines cutting-edge AI technology with real-time market data 
              to provide you with unparalleled investment insights.
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {features.map((feature, index) => (
              <Link 
                key={index}
                to={feature.link}
                className="card group cursor-pointer"
                style={{ animationDelay: `${index * 0.1}s` }}
              >
                <div className="text-center">
                  <div className="text-5xl mb-4 group-hover:animate-pulse">{feature.icon}</div>
                  <h3 className="text-xl font-semibold mb-4 text-white">{feature.title}</h3>
                  <p className="text-secondary leading-relaxed">{feature.description}</p>
                  <div className="mt-6">
                    <span className="text-blue-400 group-hover:text-blue-300 font-medium transition-colors">
                      Learn More →
                    </span>
                  </div>
                </div>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Testimonial/Trust Section */}
      <section className="py-20 bg-gray-800">
        <div className="container">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div>
              <h2 className="heading-2 mb-6">Trusted by Smart Investors</h2>
              <p className="text-lg text-secondary mb-8">
                "The AI advisor has completely transformed how I approach investing. 
                The insights are incredibly detailed and the recommendations have 
                consistently outperformed my expectations."
              </p>
              <div className="flex items-center space-x-4">
                <div className="w-12 h-12 bg-gradient-to-r from-blue-500 to-purple-600 rounded-full flex items-center justify-center">
                  <span className="text-white font-bold">JD</span>
                </div>
                <div>
                  <div className="font-semibold text-white">John Doe</div>
                  <div className="text-sm text-muted">Portfolio Manager</div>
                </div>
              </div>
            </div>
            
            <div className="relative">
              <img 
                src="https://images.pexels.com/photos/590022/pexels-photo-590022.jpeg"
                alt="Professional Analysis"
                className="rounded-2xl shadow-2xl"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-gray-900/50 to-transparent rounded-2xl"></div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-gradient-to-r from-blue-600 via-purple-600 to-blue-800">
        <div className="container text-center">
          <h2 className="heading-2 mb-6">Ready to Elevate Your Investment Strategy?</h2>
          <p className="text-xl mb-8 max-w-2xl mx-auto">
            Join thousands of investors who trust our AI-powered platform for their financial decisions.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link to="/ask-advisor" className="btn btn-primary btn-lg">
              Get Started Free
            </Link>
            <Link to="/investments" className="btn btn-outline btn-lg">
              Explore Recommendations
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
};

export default HomePage;