import SourceInputSection from '../components/SourceInputSection';

const Home = () => {
  return (
    <div className='min-h-screen bg-slate-100'>
      <div>
        <h2 className='text-3xl font-bold pt-10 pl-5'>Transcript Summarizer</h2>
        <p className=' mt-1 ml-5 text-lg'>Summarize your transcript/videos with ease</p>
      </div>
    
      <SourceInputSection />
    </div>
  );
};

export default Home;