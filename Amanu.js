import React, { useState } from 'react';

export default function LoginPage() {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    if (!formData.email || !formData.password) {
      setError('እባክዎን ሁሉንም መስኮች ይሙሉ።');
      return;
    }

    setLoading(true);

    try {
      // API Login Call እዚህ ጋር ይገባል
      console.log('Login attempt:', formData);
      
      // Simulation delay
      await new Promise((resolve) => setTimeout(resolve, 1000));
      
      alert('በተሳካ ሁኔታ ገብተዋል!');
    } catch (err) {
      setError('የተሳሳተ ኢሜይል ወይም የይለፍ ቃል!');
    } finally {
      setLoading(false);
    }
  };

  return (
                            ወደ መለያዎ ይግቡ                          አዲስ ነዎት?{' '}                  
    አዲስ መለያ ይክፈቱ                                        
                    {error && (                              {error}           
               )}    
             
                         ኢሜይል / Email                         
                       
                                                                የይለፍ ቃል / Password    
                        
              
            
            

                                                             
                   አስታውሰኝ                                                                           
   ይለፍ ቃል ረስተዋል?                                              
                       
               {loading ? 'እየገባ ነው...' : 'ይግቡ (Sign In)'}                                           
             );}
