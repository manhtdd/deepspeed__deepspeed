from .bert import DS_BERTContainer, HFBertLayerPolicy
from .bloom import DS_BloomContainer, BLOOMLayerPolicy
from .distil_bert import DS_DistilBERTContainer, HFDistilBertLayerPolicy
from .gpt2 import DS_GPT2Container, HFGPT2LayerPolicy
from .gptj import DS_GPTJContainer, HFGPTJLayerPolicy
from .gptneo import DS_GPTNEOContainer, HFGPTNEOLayerPolicy
from .gptneox import DS_GPTNEOXContainer, GPTNEOXLayerPolicy
from .megatron_gpt import DS_MegatronGPTContainer, MegatronLayerPolicy
from .megatron_gpt_moe import DS_MegatronGPTMoEContainer, MegatronMoELayerPolicy
from .opt import DS_OPTContainer, HFOPTLayerPolicy
from .clip import DS_CLIPContainer, HFCLIPLayerPolicy
from .unet import UNetPolicy
from .vae import VAEPolicy

try:
    import transformers
    supported_models = {
        transformers.models.bloom.modeling_bloom.BloomModel,
    }
except:
    supported_models = {None}