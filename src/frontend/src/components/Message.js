import React from 'react';

function Message({variant, children}) {
  return (
    <div className={variant}>
      {children}
    </div>
  );
};

export default Message;