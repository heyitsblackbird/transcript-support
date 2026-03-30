import Summary from '@/components/Summary';
import SourceInputSection from '@/components/SourceInputSection';
import React, { useState } from 'react';

const Home = () => {
  const [summary, setSummary] = useState("");
  return (
    <div className='min-h-screen bg-slate-100'>
      <div>
        <h2 className='text-3xl font-bold pt-10 pl-5'>Transcript Summarizer</h2>
        <p className=' mt-1 ml-5 text-lg'>Summarize your transcript/videos with ease</p>
      </div>
      <div className='flex items-baseline'>
        <SourceInputSection setSummary={setSummary} />
        <Summary summary={summary} />
      </div>
    </div>
  );
};

export default Home;