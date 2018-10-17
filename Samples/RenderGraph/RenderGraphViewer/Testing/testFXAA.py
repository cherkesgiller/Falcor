def render_graph_testFXAA():
	testFXAA = createRenderGraph()
	DepthPass = createRenderPass("DepthPass", {'depthFormat': Format.D32Float})
	testFXAA.addPass(DepthPass, "DepthPass")
	SkyBox = createRenderPass("SkyBox")
	testFXAA.addPass(SkyBox, "SkyBox")
	ForwardLightingPass = createRenderPass("ForwardLightingPass", {'sampleCount': 1, 'enableSuperSampling': False})
	testFXAA.addPass(ForwardLightingPass, "ForwardLightingPass")
	FXAA = createRenderPass("FXAA")
	testFXAA.addPass(FXAA, "FXAA")
	BlitPass = createRenderPass("BlitPass", {'filter': Filter.Linear})
	testFXAA.addPass(BlitPass, "BlitPass")
	testFXAA.addEdge("FXAA.dst", "BlitPass.src")
	testFXAA.addEdge("ForwardLightingPass.color", "FXAA.src")
	testFXAA.addEdge("DepthPass.depth", "ForwardLightingPass.depth")
	testFXAA.addEdge("DepthPass.depth", "SkyBox.depth")
	testFXAA.addEdge("SkyBox.target", "ForwardLightingPass.color")
	testFXAA.markOutput("BlitPass.dst")
	return testFXAA

testFXAA = render_graph_testFXAA()