const { get } = require("http");
const os = require("os");

// console.log(os.hostname());
// console.log(os.platform());

// const getInfo = () => {
//   console.log(os.platform(), os.homedir(), os.hostname());
// };
// getInfo();

// console.log(Object.keys(os));

const getInfo2 = () => {
  console.log(os.freemem(), os.networkInterfaces(), os.userInfo());
};
getInfo2();

const getInfo3 = () => {
  return [os.freemem(), os.networkInterfaces(), os.userInfo()];
};
getInfo3();
