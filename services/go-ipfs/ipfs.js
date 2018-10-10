let ipfsAPI = require('ipfs-api')
let ipfs = ipfsAPI('localhost', '5001', {protocol: 'http'})
function upload (data) {
	const buffer = Buffer.from('this is a demo')
	ipfs.add(buffer)
		.then(rsp => console.log(rsp[0].hash))
		.catch(err => console.error(err))
}
export {
	upload
}