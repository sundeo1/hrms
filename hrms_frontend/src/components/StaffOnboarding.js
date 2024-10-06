import React, { useState } from 'react';
import OtpRequest from './OtpRequest';
import OtpVerification from './OtpVerification';
import StaffRegistration from './StaffRegistration';

const StaffOnboarding = () => {
  const [step, setStep] = useState(1); // Step control
  const [mobileNumber, setMobileNumber] = useState('');
  const [verifiedOtp, setVerifiedOtp] = useState('');

  return (
    <div>
      {step === 1 && <OtpRequest setStep={setStep} setMobileNumber={setMobileNumber} />}
      {step === 2 && <OtpVerification setStep={setStep} mobileNumber={mobileNumber} setVerifiedOtp={setVerifiedOtp} />}
      {step === 3 && <StaffRegistration mobileNumber={mobileNumber} verifiedOtp={verifiedOtp} />}
    </div>
  );
};

export default StaffOnboarding;
