import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import math, copy, time
class EncoderDecoder(nn.Module):
    def __init__(self,encoder,decoder,src_embed,target_embed,generator):
        super(EncoderDecoder,self).__init__()
        self.encoder=encoder
        self.decoder=decoder
        self.src_embed=src_embed
        self.target_embed=target_embed
        self.generator=generator
    def forward(self,src,tgt,src_mask,tgt_mask):
        return self.decode(self.encode(src,src_mask),src_mask,tgt,tgt_mask)
    def encode(self ,src,src_mask):
        return self.encoder(self.src_embed(src),src_mask)
    def decode(self,memory,src_mask,tgt,tgt_mask):
        return self.decoder(self.target_embed(tgt),memory,src_mask,tgt_mask)