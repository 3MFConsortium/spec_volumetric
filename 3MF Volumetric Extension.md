#
# 3MF Volumetric Extension

## Specification & Reference Guide



| **Version** | 0.6.0 |
| --- | --- |
| **Status** | Pre-release |

**Note**

This version of the 3MF Volumetric Extension is a pre-release version. Consumers and producers can implement this version and use it, however, future version of this specification, in particular the "Published" version, might not be backwards compatible to this version.


## Table of Contents

- [Preface](#preface)
  * [About this Specification](#11-about-this-specification)
  * [Document Conventions](#12-document-conventions)
  * [Language Notes](#13-language-notes)
  * [Software Conformance](#14-software-conformance)
- [Part I: 3MF Documents](#part-i-3mf-documents)
  * [Chapter 1. Overview of Additions](#chapter-1-overview-of-additions)
  * [Chapter 2. 3D Image](#chapter-2-3d-image)
  * [Chapter 3. Channel from 3D Image](#chapter-3-channel-from-3d-image)
  * [Chapter 4. Volumetric Stack](#chapter-4-volumetric-stack)
  * [Chapter 5. Volumetric Data](#chapter-5-volumetric-data)
- [Part II. Appendices](#part-ii-appendices)
  * [Appendix A. Glossary](#appendix-a-glossary)
  * [Appendix B. 3MF XSD Schema for the Volumetric Extension](#appendix-b-3mf-xsd-schema-for-the-volumetric-extension)
  * [Appendix C. Standard Namespace](#appendix-c-standard-namespace)
  * [Appendix D: Example file](#appendix-d-example-file)
- [References](#references)



# Preface

## 1.1. About this Specification

![Volumetric image](images/volumetric_image1.png)

This 3MF volumetric specification is an extension to the core 3MF specification. This document cannot stand alone and only applies as an addendum to the core 3MF specification. Usage of this and any other 3MF extensions follow an a la carte model, defined in the core 3MF specification.

Part I, "3MF Documents," presents the details of the primarily XML-based 3MF Document format. This section describes the XML markup that defines the composition of 3D documents and the appearance of each model within the document.

Part II, "Appendices," contains additional technical details and schemas too extensive to include in the main body of the text as well as convenient reference information.

The information contained in this specification is subject to change. Every effort has been made to ensure its accuracy at the time of publication.

This extension MUST be used only with Core specification version 1.3. or higher.


## 1.2. Introduction
Volumetric Modeling is an efficient approach to encode geometrical shapes and spatial properties and is based on a volumetric description.
Traditional, explicit modeling methodologies are based on surfaces (e.g. NURBS, triangular meshes) that describe the boundaries of an object. This is illustrated in Figure 1-1 a): a NURBS surface delimitates a region of space. Figure 1-1 b) shows a triangular mesh that describes the same surface. In each case, the top part of the described object is being shown transparently to allow viewing the "inside" of the described object.

The volumetric modeling approach relies on a mathematical, field-based description of the whole volume of the object. This is illustrated in Figure 1-1 c). Every point in space has a scalar (gray-scale) value. The iso-surface at value 0 describes the surface of the same object as in Figure 1-1 a). A section of this iso-surface is indicated by the blue line.

The true advantage of volumetric modeling shows when properties of an object vary in space gradually, e.g. color or material-distribution and -composition of an object vary in space. E.g. in Figure 1-2 a) the object has a uniform color except for a red stripe at the front-left surface. Note that not only the surface, but also the interior volume has a non-uniform color in this region. Figure 1-2 b) shows a distribution of three different materials, indicated by three different colors, red, blue and green.

This is only a brief illustration of the volumetric modeling approach to geometric design and more information can be found in [references](#references) \[1\] and \[2\].

_Figure 1-1. Explicit (a) and (b) vs. implicit (c) representation_
![Explicit vs. implicit representation](images/explicit_vs_implicit.png)

_Figure 1-2. Spatially varying properties_
![Volumetric properties](images/spatially_varying_property.png)

## Document Conventions

See [the standard 3MF Document Conventions documentation](https://github.com/3MFConsortium/spec_resources/blob/master/document_conventions.md).

## Language Notes

See [the standard 3MF Language Notes documentation](https://github.com/3MFConsortium/spec_resources/blob/master/language_notes.md).

## Software Conformance

See [the standard 3MF Software Conformance documentation](https://github.com/3MFConsortium/spec_resources/blob/master/software_conformance.md).


# Part I. 3MF Documents

## Chapter 1. Overview of Additions

_Figure 1-1 Overview of model XML structure of 3MF with volumetric additions_
![Overview of model XML structure of 3MF with volumetric additions](images/overview-of-additions.png)

This document describes new elements, each of which is OPTIONAL for producers, but MUST be supported by consumers that specify support for this volumetric extension of 3MF.

The central idea of this extension is to enrich the geometry notion of 3MF with volumetric elements that can represent spatially varying properties which are quite inefficient to handle with a mesh representation, especially in cases where the variation is continuous in space.

This extension is meant to be an exact specification of geometric, appearance, material and in fact arbitrary properties, and consumers MUST interpret it as such. However, the intent is also to enable editors of 3MF files to use the designated data structures for efficient interoperability and post-processing of the geometry and properties described in this extension.

A producer using the boundary element of the volumetric specification MUST mark the extension as required, as described in the core specification. Producers only using the other specification elements, in particular color-, composite- and property-elements, MAY mark the extension as required. Consumers of 3MF files that do not mark the volumetric extension as required are thus assured that the geometric shape of objects in this 3MF file are not altered by the volumetric specification.


# Chapter 2. 3D Image

## 2.1 3D Image

Element **\<image3d>**

![Image3D XML structure](images/element_image3d.png)

| Name   | Type   | Use | Default | Annotation |
| --- | --- | --- | --- | --- |
| id | ST\_ResourceID | required | | Specifies an identifier for this image3d resource. |
| name | xs:string | | | 3d image resource name used for annotations purposes. |
| rowcount | xs:positiveinteger | required || Number of pixel rows in all child \<image3dsheet>-elements. |
| columncount | xs:positiveinteger | required || Number of pixel columns in all child \<image3dsheet>-elements. |
| sheetcount | xs:positiveinteger | required || Number of \<image3dsheet>-elements within this \<image3d> element. |

Volumetric data can be encoded as 3d images that consist of voxels. Each \<image3d> element is assumed to represent a finite voxel grid from which data can be sampled at any point. Volumetric images can be embedded inside a 3MF file using groups of PNG images that represent a stack of images.

All \<image3dsheets> within an image3d MUST have the same number of rows and columns that is specified in the rowcount and columncount-attributes, respectively. rowcount, columncount and sheetcount MUST not exceed 1024^3, each. The total number of voxels MUST be limited by 1024^5. There MUST be exactly sheetcount \<image3dsheet>-elements under \<image3d> that are implicitly ordered starting with index 0.

Image3D objects, and thus the underlying \<image3dsheet> elements, MUST follow one of the input pixel layouts shown in the table below. All image3dsheets within an image3d MUST have the same input pixel layouts, and each channel MUST have the same bit-depth across all image3dsheets.

The following table shows the logical interpretation of sampling the "R", "G", "B" or "A"-channel depending on the input pixel layouts. The meaning of symbols is as follows: R – red, G – green, B – blue, A – alpha, Y – greyscale.

| Input pixel layout | | | | | |
| --- | --- | --- | --- | --- | --- |
| RGBA | R | G | B | A |
| RGB | R | G | B | 2^bitdepth-1 |
| YA | Y | Y | Y | A |
| Y | Y | Y | Y | 2^bitdepth-1 |

For example, if the specification says that a certain value is sampled from the image’s R channel, but the referenced image is only monochromatic, then the greyscale channel is interpreted as the R color channel. Similarly, color values sampled from a monochromatic image are interpreted as if all R, G, B color channels shared the same greyscale value. If there is no alpha channel present in the image, the highest possible value `2^bitdepth-1` MUST be used.

The \<image3d>-element defines a voxel grid of values (e.g. RGB, grey-Alpha, grey) values distributed in a cuboid ({0,1,...,rowcount-1} x {0,1,...,columncount-1} x {0,1,...,sheetcount-1}). The left-front-bottom corner of this grid corresponds to the (0,0,0)-UVW coordinate when this 3D Image is being sampled, whereas the right-back-top corner corresponds to the (1,1,1) UVW-coordinate. Each \<image3dsheet> corresponds to one PNG-file in the package. Figure 2-1 a) illustrates a voxel grid with `rowcount=3`, `columncount=4` and `sheetcount=2` voxels. Voxel indices are shown as bold black triple, the UVW-coordinate values as red triples.
Figure 2-1b) illustrates the voxel indices and the UVW-values throughout the first \<image3dsheet>, Figure 2-1 c) illustrates these quantities throughout the second \<image3dsheet>. A voxel index triple `(i,j,k)` corresponds to a voxel with rowindex `i`, columnindex `j` and sheetindex `k`.

__Note__: The columnindex (`j`) relates to the UVW-coordinate `U`, whereas the rowindex `i` relates to the UVW-coordinate `V`. This definition is inline with the
Materials and Properties specification https://github.com/3MFConsortium/spec_materials/blob/1.2.1/3MF%20Materials%20Extension.md#chapter-6-texture-2d.

The sampling rules for UVW values are determined by the filter-rule, see the filter attribute and the behaviour for UVW-values outside the unit-cube are determines by the tilestyle attributes [of the Channel from Image3D XML structure](#chapter-3-channel-from-3d-image), respectively.

_Figure 2-1: Voxel indixes and UVW-texture space of a sample voxel grid: a) shows a voxel grid of 3x4x2 voxels. b) shows a section view of the bottom voxels, c) shows a section view of the top voxels. The orange voxel at the right, front and bottom of a) has rowindex=2, columnindex=3 and sheetindex=0. d) shows the voxelcenters of this configuration._
![Voxel indices and UVW-texture space of a sample voxel grid](images/image3dcoordinates.png)

## 2.1.1 File Formats
PNG images can provide acceptable compression and bit-depth for the levelset-function, color information, material mixing ratios or arbitrary property information.

The following describes recommendations for the channel bit depth of PNG images used in this specification and is based on the nomenclature in the specification of the Portable Network Graphics (PNG, https://www.w3.org/TR/PNG) format.

- Color information, material mixing ratios and arbitrary properties can be deduced from PNG images with arbitrary channel depth. It is RECOMMENDED to store color into RGB-channels within a PNG.

- It is RECOMMENDED to store image information that will be used as levelset-function to represent a boundary in PNGs with one channel only. A typical approach to encode this levelset information is to encode the signed distance field of the boundary of the object in this channel. A different option is to deduce the levelset-function from a channel with binary values, i.e. from images of image type "greyscale" with bit-depth of 1 or an indexed-color with bit depths of 1.

To achieve high accuracy, producers SHOULD store such information in image channels with bit depth of 16. Most professional image editing tools and standard implementations of the PNG format support channels with 16 bit.


## 2.1.2 OPC package layout
It is RECOMMENDED that producers of 3MF Documents use the following part naming convention:

Paths of  \<image3dsheet> SHOULD consist of four segments. "/3D/volumetric/" as the first two segments, the name of a image3d-element that references this  \<image3dsheet> as third segment (for example "/3D/volumetric/mixingratios/", and the name of the image3dsheet as last segment (for example "sheet0001.png"). The 3D Texture part that is the  \<image3dsheet> MUST be associated with the 3D Model part via the 3D Texture relationship.

This implies that all  \<image3dsheet> parts for an image3d-object SHOULD be located in the same OPC folder.

_Figure 2-3: OPC package layout_
![OPC package layout](images/OPC_overview.png)

## 2.2 3D Image Sheet

Element **\<image3dsheet>**

![image3dsheet XML structure](images/element_image3dsheet.png)

| Name   | Type   | Use | Default | Annotation |
| --- | --- | --- | --- | --- |
| path | ST\_UriReference | required | | Specifies the OPC part name (i.e. path) of the image data file |
| valueoffset | ST\_Number | | 0.0 | Specifies a numerical offset for the values obtained from any channel on this `image3dsheet`. |
| valuescale | ST\_Number | | 1.0 | Specifies a numerical scaling for the values obtained from any channel on this `image3dsheet`. |

Each \<image3dsheet> element has one required attribute. The path property determines the part name (i.e. path) of the 2D image data (see chapter 6 of the Materials & Properties Extension specification for more information).

The `valueoffset` and `valuescale` determine how the numerical values of any channel within the referenced PNG-file shall be interpreted.
If a channel in the image-file of this \<image3dsheet> holds a numerical value `V`, it needs to be sampled as `V' = V*valuescale + valueoffset`.
Specifying different `valueoffset` and `valuescale`-attributes for different \<image3dsheet>s is optional, but allows producers to more efficiently encode values in different regions of an object.

Any interpolation of values of an \<image3dsheet>-element (c.f. the [**filter** attribute on the Channel From Image3D](#chapter-3-channel-from-3d-image)) MUST be performed on the rescaled values `V'` according to the formula above. This is relevant if two subsequent \<image3dsheet>-elements have different values for `valueoffset` or `valuescale`.


# Chapter 3. Channel from 3D Image
 
Element type
**\<channelfromimage3d>**

![Channel from Image3D XML structure](images/element_channelfromimage3d.png)

| Name   | Type   | Use | Default| Annotation |
| --- | --- | --- | --- | --- |
| id | ST\_ResourceID | required | | The resource id of this ChannelFromImage3D resource |
| image3did | ST\_ResourceID | required | | Specifies the id of the 3d image resource |
| channel | ST\_ChannelName | required | | Specifies which channel to reference in the 3d image resource |
| transform | ST\_Matrix3D | required | | Transformation of the channel coordinate system into the \<image3d> coordinate system |
| valueoffset | ST\_Number |  | 0.0 | Specifies a numerical offset for the values obtained from the `channel` within the `image3d` referred to by this CT_ChannelFromImage3D |
| valuescale | ST\_Number | | 1.0 | Specifies a numerical scaling for the values obtained from the `channel` within the `image3d` referred to by this CT_ChannelFromImage3D. |
| filter |ST\_Filter | | linear | "linear" or "nearest" neighbor interpolation |
| tilestyleu | ST\_TileStyle | Required | | Determines the behavior of the sampler for texture coordinate u outside the [0,1] range |
| tilestylev | ST\_TileStyle | Required | | Determines the behavior of the sampler for texture coordinate v outside the [0,1] range |
| tilestylew | ST\_TileStyle | Required | | Determines the behavior of the sampler for texture coordinate w outside the [0,1] range |

Elements of type \<CT_ChannelFromImage3D> define the way in which individual channels from volumetric image resources can be referenced inside the volumetric layer elements. Each channel reference MUST contain a resource id that maps to an actual \<image3d> element.

In addition, the elements of type \<CT_ChannelFromImage3D> MUST contain a \<ST\_ChannelName> attribute which determines which channel to pick from the \<image3d> element. This attribute must be any of the reserved channel names (i.e. "R", "G", "B", or "A"). 

**channel**:

The channel-attribute determines which channel to reference in the 3d image resource. Note that attributes of type \<ST\_ChannelName> are case-sensitive.

**tilestyle-u, -v or -w**:

MUST be one of "wrap", "mirror",  "clamp" and "none". This property determines the behavior of the sampler of this channel for 3d texture coordinates (u,v,w) outside the [0,1]x[0,1]x[0,1] cell. The different modes have the following interpretation (for s = u, s = v, or s = w):

1. "wrap" assumes periodic texture sampling, see Figure 3-1 a). A texture coordinate s that falls outside the [0,1] interval will be transformed per the following formula:
</br>s’ = s – floor(s)

2. "mirror" means that each time the texture width or height is exceeded, the next repetition of the texture MUST be reflected across a plane perpendicular to the axis in question, see Figure 3-1 b). This behavior follows this formula:
</br>s’ = 1 - abs( s - 2 * floor(s/2) - 1 )

3. "clamp" will restrict the texture coordinate value to the [0,1] range, see Figure 3-1 c). A texture coordinate s that falls outside the [0,1] interval will be transformed according to the following formula:
</br>s’ = min(1, max(0,s))

4. "none" will discard the \<CT_ChannelFromImage3D>'s value if the 3d texture coordinate s falls outside the [0,1] range. This means, when blending volumetric layers, no blending of values takes place if this \<CT_ChannelFromImage3D> is sampled outside the [0,1]-range. This is useful if a 3d texture is used as masking channel for a volumetric decal of sorts that affects only a limited region in the volume.

	_Figure 3-1: Illustration of different tilestyles. a) tilestyle wrap illustrated throughout the second \<image3dsheet>. b) tilestyle mirror illustrated throughout the second \<image3dsheet>. c) tilestyle clamp along the u-direction illustrated throughout the second \<image3dsheet>_
	![Tilestyles](images/tilestyle_all.png)

**transform**:
Transformation of the channel coordinate system into the \<image3d> coordinate system.
If this channel is being sampled at position `(x,y,z)` (e.g. from within a volumetric stack), the underlying \<image3d> must be sampled at normalized texture coordinates `(u,v,w) = T*(x,y,z)`.

**filter**:
The filter attribute defines the interpolation method used when a \<channelfromimage3d> is being sampled. This is illustrated in Figure 3-3.

- If the interpolation method of an elements of type \<channelfromimage3d> is "nearest", sampling it at an arbitrary (u,v,w) returns the floating point value defined by the closest point (u',v',w') to (u,v,w) which transforms back to a voxel center in the 3D image resource.

- If the interpolation method of an elements of type \<channelfromimage3d> is "linear", sampling it at an arbitrary (u,v,w) returns the floating point defined by trilinearly interpolating between the eight closest points coordinates which transforms back to voxel centers in the 3D image resource.

    _Figure 3-3: filter attributes "nearest" (a) and "linear" (b). The image3d of Figure 2-1 used is reused in this example. The region shown is clipped at w=0.75, v=1/6 and u=2. The grey wireframe box indicates the UVW unit box. The tilesyle is "wrap" in all directions.
    ![Tilestyle mirror](images/filter.png)

**`offsetvalue` and `scalevalue`**:

The values `V'` sampled from the \<image3d> are linearly scaled via `offsetvalue` and `scalevalue` giving a sampled value `V'' = V'*scalevalue + offsetvalue`


__Note__: Summing up [chapters 2](#chapter-2-3d-image) and [3](#chapter-3-channel-from-3d-image): the \<image3d> and the \<channelfromimage3d>-elements describe a scalar volumetric texture. Other file formats like OpenVDB or OpenEXR offer similar functionality, and are more efficient at doing so. However, their use in a manufacturing environment is hard as these formats are conceptually more complex and harder to implement. Therefore, this specification relies on the human readable and conceptually simpler stack of PNGs. Later versions of this extension, or private extension of the 3MF format MAY use different 3D image formats to encode volumetric textures and benefit from their advanced features.
The remainder of this specification deals with the mapping of these volumetric textures onto mesh-objects in a 3MF file and giving these textures a meaning for additive manufacturing processes. Replacing \<image3d> and the \<channelfromimage3d> would not affect the remaining parts of this specification.

# Chapter 4. Volumetric Stack

Element **\<volumetricstack>**

![volumetricstack XML structure](images/element_volumetricstack.png)

| Name   | Type   | Use | Default | Annotation |
| --- | --- | --- | --- | --- |
| id | ST\_ResourceID | required | | Specifies the id of this volumetricstack |

The volumetric stack is a resource within a 3MF model that defines how volumetric data
from multiple \<CT_ChannelFromImage3D> is composited to yield multiple custom scalar field in three dimensions (\<dstchannel>). This custom scalar field of a \<volumetricstack> element can then be used to define volumetric properties inside the \<volumedata>-element of an object, see the [volumedata-element](#chapter-5-volumetric-data).

1. It defines multiple destination channels, \<dstchannel>-elements. Each destination channel is a scalar field in 3d, whose values can be retrieved by sampling this volumetricstack.

2. The sampled values of each destination channel are built up by blending multiple layers, the \<volumetriclayer>-elements. This allows e.g. boolean operations on the scalar fields provided by different \<channelfromimage3d> elements.

The volumetricstack element MUST contain at least one \<dstchannel> child element and MUST NOT contain more than 2^16-1 \<dstchannel> child-elements. The volumetricstack element MUST NOT contain more than 2^16-1 \<volumetriclayer> child-elements.

## 4.1 Destination channel element

Element **\<dstchannel>**

![dstchannel XML structure](images/element_dstchannel.png)

| Name   | Type   | Use | Default | Annotation |
| --- | --- | --- | --- | --- |
| name | ST\_ChannelName | required | | Specifies the name of this destination channel |
| background | ST\_Number | required | | Specifies the background value of this channel |

A destination channel specifies a name of a channel that can be sampled from a volumetricstack element.
The background value is the value that serves as a base for the blending that takes place in the \<volumetriclayer> elements within the \<volumetricstack>-element.

The names of \<dstchannel>-elements must be unique within a \<volumetricstack>-element.

## 4.2 Volumetric Layer element

Element **\<volumetriclayer>**

![volumetriclayer XML structure](images/element_volumetriclayer.png)

| Name   | Type   | Use | Default | Annotation |
| --- | --- | --- | --- | --- |
| blendmethod | ST\_BlendMethod | required | | Determines how this layer is applied to its sublayers. Allowed values are "weightedsum", "multiply", "min", "max" or "mask". |
| srcalpha | ST\_Number | | | Numeric scale factor for the source layer. Required if blendmethod is "weightedsum". |
| dstalpha | ST\_Number | | | Numeric scale factor for the destination layer. Required if blendmethod is "weightedsum".  |
| maskid | ST\_ResourceId | | | The resource id of a \<channelfromimage3d> resource which shall be used for masking. Required if blendmethod is "mask".  |

Each \<volumetriclayer>-element modify the accumulated value of the destination channels of a volumetric stack. This modification is defined by the following attributes:

**blendmethod**: controls according to which formula the current layer (known as the source layer) is blended with the layers below it or with the stack’s background value.

Let "s" denote the value of the source channel, "d" the current value of the destination channel, then the modified value of the destination channel "d'" after blending is calculated according to the blendmethod:

- "weightedsum":

    d' = src_alpha * s + dst_alpha * d

    **srcalpha**: is a scalar value which is multiplied with the sampled values in the source layer during the blending process.

    **dstalpha**: is a scalar value which is multiplied with the sampled values in the destination during the blending process.
    
    The producer of a 3MF file is responsible to choose parameters srcalpha and dstalpha, such that sampling the blended value of a channel, e.g. a physical property, is sensible.

- "multiply":

    d' = s * d

- "min" or "max":
   
    d' = min(s,d) or d' = max(s,d)
    
    Blending methods "min" and "max" are useful to capture boolean operations (union and intersection, respectively) between fields representing levelset functions.

- "mask":

    The blendmethod "mask" provides a means to use another channel as a volumetric decal that only affects a region of complex shape within the volume.

    d' = m * s + (1 - m) * d
    
    Here, m is the value of the channel provided by the \<channelfromimage3d> referred to by the "maskid" attribute of this volumetriclayer.
    
    __Note__: The blendmethod "mask" implements the same formula as the blendmethod "mix" for the rgb-values of an \<multiproperties>-element in the [Materials and Properties Extension specification, Chapter 5](https://github.com/3MFConsortium/spec_materials/blob/1.2.1/3MF%20Materials%20Extension.md#chapter-5-multiproperties).


Figure 4-1 shows an example of two layers within a volumetric stack and the result using various blending functions with different source and destination alpha values.
A volumetriclayer MUST contain at least one \<channelmapping> element. The dstchannel attribute of each \<channelmapping> within a volumetriclayer element MUST match a \<dstchannel> element within this \<volumetriclayer>.
The name of each \<dstchannel> element MUST occur at most once as dstchannel attribute in one of the \<channelmapping>.

Destination channels that are not mentioned as dstchannel attribute in this list are not modified by this \<volumetriclayer>.

_Figure 4-1: Example of different blending methods and parameters and src- or dst-alpha values_
![Example of different blending methods and parameters and src- or dst-alpha values](images/blending.png)

## 4.3 Channelmapping element
Element **\<channelmapping>**

![channelmapping XML structure](images/element_channelmapping.png)

| Name   | Type   | Use | Default | Annotation |
| --- | --- | --- | --- | --- |
| sourceid | ST\_ResourceID | required | | The resource id of a ChannelFromImage3D resource |
| dstchannel | ST\_ChannelName | required | | Name of the destination channel that should be manipulated by this channelmapping within this volumetric layer |

# Chapter 5. Volumetric Data

## 5.1. Volumetric Data extension to Mesh
 
Element **\<mesh>**

![mesh XML structure](images/element_mesh.png)

The volumetric data \<volumedata> element is a new OPTIONAL element which extends the root triangular mesh representation (i.e. \<mesh> element).


## 5.2. Volumetric Data
 
Element **\<volumedata>**

![volumedata XML structure](images/element_volumedata.png)

The \<volumedata> element references the volumetric data given by \<volumetricstack>-elements and defines how their various channels are mapped to specific properties within the interior volume of the enclosing mesh.
Volumedata MUST only be used in a mesh of object type "model" or "solidsupport". This ensures that the \<mesh> defines a volume.
Moreover, the volumedata-element MUST not be used in a mesh that is referenced as "originalmesh" by any other mesh.

The volumedata element can contain up to one \<boundary> child element, up to one \<composite> child element,
up to one \<color> element, and an arbitrary number of \<property> elements.

The child elements modify the enclosing \<mesh> in two fundamentally different ways:
1. the child \<boundary> element (if it exists) determines the geometry of the \<mesh> object.
2. the other child elements modify color, material composition and other arbitrary properties of the \<mesh> object.

We need to define the clipping surface of a mesh with a \<volumedata> element. The clipping surface is defined as follows:
1. If no \<boundary> element exists, the clipping surface is defined by the surface of the enclosing \<mesh> element. This implicitly takes into account any geometry defined by e.g. the beamlattices specification.
2. If the \<boundary> element exists, the clipping surface is defined by the intersection of the geometry from 1. and the interior of the levelset-channel used in the \<boundary> element.

This clipping surface trims any volumetric data defined therein. Any data outside the clipping surface MUST be ignored. The geometry that should be printed is defined by the interior of the clipping surface.

Volumetric content is always clipped to the clipping surface of the mesh that embeds it. If a property (color, composite or properties) defined at the surface of an object conflicts with the property within the object defined by this extension, a surface layer should be defined with a thickness as small as possible to achieve the surface property on the outside of the object. Outside of this thin surface region, the volumetric property should be applied everywhere within the object.

The properties at surface regions that are not explicitly specified are instead given by the volumetric properties.

Conflicting properties must be handled as follows:
1. Producers MUST not define colors, materials or properties via child elements of the \<volumedata> element that are impossible on physical grounds (e.g. non-conducting copper).
2. Consumers that read files with properties that cannot be realized due to limitations specific to them (e.g. a specific manufacturing device that does not support a material in a specific color), SHOULD raise a warning, but MAY handle this in any appropriate way for them. If there is an established process between Producer and Consumer, resolution of such conflicts SHOULD be performed e.g. via negotiation through printer capabilities and a print ticket.

__Note__: In the case where objects with different volumedata elements, only the volumedata elements from last object can be used.
This makes sure that volumedata elements of an overlapped object do not determine any volumedata elements of an overlapping object. Figure 5-1 illustrates this behavior.

_Figure 5-1: a) Mesh object A (circle) with volumedata element X. b) Mesh object B (rectangle) with volumedata element Y. The mesh objects are defined in the order A-B. c) shows the volume defined by the overlapped mesh objects. d) shows volumedata element X in object A, and volumedata element Y in object B. The table lays out how these volumedata elements are sampled at positions p1 to p4._
![Illustration of overlapping meshes with volumedata elements](images/overlap_properties.png)


### 5.2.1 Boundary element

Element **\<boundary>**

![boundary XML structure](images/element_boundary.png)

| Name   | Type   | Use | Default | Annotation |
| --- | --- | --- | --- | --- |
| sourceid | ST\_ResourceID | required | | ResourceID of the volumetricstack that holds a channel that encodes the boundary as a levelset |
| channel | ST\_ChannelName | required | | Name of the channel that holds a levelset function which defines the boundary |
| solidthreshold | ST\_Number | | 0.0 | Determines the values of the levelset function which are considered inside or outside the specified object  |
| transform | ST\_Matrix3D | required | | Transformation of the object coordinate system into the volumetricstack coordinate system |

The boundary element is used to describe the interior and exterior of an object via a levelset function.

**sourceid** and **channel**:

The levelset function is given by the "dstchannel" within the \<volumetricstack>
with resource id matching the sourceid-attribute and with name matching the "channel"-attribute of the \<boundary>-element.

**solidthreshold**:

The value of the levelset function `f` at a position `(x,y,z)` and the solidthreshold determine whether (x,y,z) is inside or outside the specified object:
 - If `f<=solidthreshold`, then `(x,y,z)` is inside the specified object.
 - If `f>solidthreshold`, then `(x,y,z)` is outside the specified object.

**transform**:

The transformation of the object coordinate system into the \<volumetricstack> coordinate system.
If the boundary-channel of the enclosing \<mesh> is being sampled at position `(x,y,z)` in the mesh's local object coordinate system, the referenced channel in the \<volumetricstack> must be sampled at position `(x',y',z') = T*(x,y,z)`.
See Figure 5-2 for an illustration of this transform in the sampling process.

### 5.2.2 Color element

Element **\<color>**

![color XML structure](images/element_color.png)

| Name   | Type   | Use | Default | Annotation |
| --- | --- | --- | --- | --- |
| sourceid | ST\_ResourceID | required | | ResourceID of the volumetricstack that holds the channels to be used in the child color elements. |
| transform | ST\_Matrix3D | required | | Transformation of the object coordinate system into the volumetricstack coordinate system |

The \<color> element is used to define the color of the object.
The color MUST be interpreted in linearized sRGB color space as defined in the Materials and Properties specification https://github.com/3MFConsortium/spec_materials/blob/1.2.1/3MF%20Materials%20Extension.md#12-srgb-and-linear-color-values. If the value of the channel of a \<red>-, \<green>- and \<blue>-element is \<0 or \>1 it has to be truncated at 0 or 1, respectively.

This specification does not capture well the properties for semi-transparent, diffusive materials. This specification is useful for defining parts with non transparent, opaque materials, e.g. for indicating wear and tear, sectioning the models and printing with non transparent materials.

The \<color>-element MUST contain exactly three \<red>-, \<green>- and \<blue>-element.

**transform**:

The transformation of the object coordinate system into the \<volumetricstack> coordinate system.
If the \<red>-, \<green>- or \<blue>-channel is being sampled at position `(x,y,z)` in the mesh's local object coordinate system, the referenced channel in the \<volumetricstack> must be sampled at position `(x',y',z') = T*(x,y,z)`.

### 5.2.2.1 Color channel elements

Elements **\<red>, \<green> and \<blue>**

![colorchannel XML structure](images/elements_redgreenblue.png)

of

Complex type **\<colorchannel>**

![colorchannel XML structure](images/ct_colorchannel.png)

| Name   | Type   | Use | Default | Annotation |
| --- | --- | --- | --- | --- |
| channel | ST\_ChannelName | required | | Source channel for the values of this color channel |

Each element instance of CT\_ColorChannel MUST have an attribute "channel" that
references a destination channel from the \<volumetricstack> with Id matching the sourceid of the parent \<color> element.

If the value of the channel of a \<red>-, \<green>- and \<blue>-element is \<0 or \>1 it has to be truncated at 0 or 1, respectively. 


## 5.2.3 Composite element

Element **\<composite>**

![composite XML structure](images/element_composite.png)

| Name   | Type | Use | Default | Annotation |
| --- | --- | --- | --- | --- |
| sourceid | ST\_ResourceID | required | | ResourceID of the volumetricstack that holds the channels used in the child \<materialmapping>-elements |
| transform | ST\_Matrix3D | required | | Transformation of the object coordinate system into the volumetricstack coordinate system |
| basematerialid | ST\_ResourceID | required | | ResourceID of the basematerial that holds the \<base>-elements referenced in the child \<materialmapping>-elements |

The \<composite> element describes a mixing ratio of printer materials at each position in space. The CONSUMER can determine the halftoning, mixing or dithering strategy that can be used to achieve these mixtures.

This element MUST contain at least one \<materialmapping> element, which will encode the relative contribution of a specific basematerial to the material mix.

**transform**:

The transformation of the object coordinate system into the \<volumetricstack> coordinate system.
If any channel of a \<materialmapping> is being sampled at position `(x,y,z)` in the mesh's local object coordinate system, the referenced channel in the \<volumetricstack> must be sampled at position `(x',y',z') = T*(x,y,z)`.

## 5.2.4 Material mapping element

Element **\<materialmapping>**

![materialmapping XML structure](images/element_materialmapping.png)

| Name   | Type   | Use | Default | Annotation |
| --- | --- | --- | --- | --- |
| channel | ST\_ChannelName | required | | Source channel for the values of this material |
| pindex | ST\_ResourceIndex | required | | ResourceIndex of the \<base>-element within the parent's associated \<basematerial>-element |

The \<materialmapping> element defines the relative contribution of a specific material to the mixing of materials in it's parent
\<composite>-element.

If the sampled value of a channel is `<0` it must be evaluated as "0".

Producers MUST NOT create files where the sum of all values in its child \<materialmapping>-elements is smaller than `10^-7`. If the total is smaller than this threshold, the mixing ratio is up to the consumer.

- If there are `N` materials, then the mixing ration of material `i` at point `X` is given by:
   ```
   value of channel i / sum(value of all N channels at point X)
   ```

Each element instance of \<CT\_MaterialMapping> MUST have an attribute "channel" that references a destination channel from the \<volumetricstack> with id matching the sourceid of the parent \<composite> element.

### 5.2.4.1 Property element

Element **\<property>**

![property XML structure](images/element_property.png)

| Name   | Type   | Use | Default | Annotation |
| --- | --- | --- | --- | --- |
| sourceid | ST\_ResourceID | required | | ResourceID of the volumetricstack that holds the channel used by this property |
| transform | ST\_Matrix3D | required | | Transformation of the object coordinate system into the volumetricstack coordinate system |
| channel | ST\_ChannelName | required | | Name of the channel that serves as source for the scalar value representing this property. |
| name | xs:QName | required | | Namespace and name of this property |
| required | xs:boolean | | false | Indicator whether this property is required to process this 3MF document instance. |

The \<property> element allows to assign any point in space a scalar value of a freely definable property. This can be used to assign, e.g. opacity, conductivity, or translucency.

**transform**:

The transformation of the object coordinate system into the \<volumetricstack> coordinate system.
If the channel of a \<property>-element is being sampled at position `(x,y,z)` in the mesh's local object coordinate system, the referenced channel in the \<volumetricstack> must be sampled at position `(x',y',z') = T*(x,y,z)`.

This specification does not provide qualified names for such properties as part of the standard volumetric namespace.
A later extension of the 3MF format might define such qualified names as part of a different extension specification or a later version of the volumetric extension specification. Producers that want to specify such properties now, SHOULD define a qualified name that can e.g. be called "http://www.vendorwwebsite.com/3mf/vendor13mfextension/2021/05".
The specifications of private namespaces (that are not ratified by the 3MF Consortium) MUST be negotiated between producer and consumer of a 3MF file.

The names of \<property>-elements MUST be unique within a \<volumedata>. This name MUST be prefixed with a valid XML namespace name declared on the <model> element.
The interpretation of the value MUST be defined by the owner of the namespace. 

If the interpretation of a property might result in a conflict with the standard volumedata-elements (boundary, color, composite) the namespace-owner MUST specify a resolution to the conflict. A producer MUST NOT create files with properties that conflict with each other.

If a physical unit is necessary, the namespace owner MUST define a unique and unambiguous physical unit system for the namespace. The unit system SHOULD be metric.

If a \<property> is marked as `required`, and a consumer does not support it, it MUST warn the user or the appropriate upstream processes that it cannot process all contents in this 3MF document instance.
Producers of 3MF files MUST mark all volumetric \<property>-elements required to represent the design intent of a model as `required`.

__Note__:

Equipped with the language elements of this specification, one can recapitulate the core concepts with an overview of the sampling process.

Figure 5-2 illustrates the 3MF elements, the different coordinate systems and transforms between them when a volume data element (in this case \<color>) is sampled in the object coordinate space.

Figure 5-2a) The object is sampled at position (+) in the object coordinate system. The clipping surface is hinted at with a wireframe. The transformation `T0` of the world coordinate system into the object coordinate system is given by the `transform`-attributes on the `item` and `component`-elements in the path that leads to this object in the `build`-hierarchy of the 3MF Core Specification (see https://github.com/3MFConsortium/spec_core/blob/1.3.0/3MF%20Core%20Specification.md#3431-item-element and https://github.com/3MFConsortium/spec_core/blob/1.3.0/3MF%20Core%20Specification.md#421-component).

Figure 5-2b) Offers a view into the \<volumetricstack> and its corresponding coordinate system. The transformation `T1` from object coordinate space to \<volumetricstack> coordinate system is given by the `transform`-element in the \<color>-element. The original clipping surface from a) is only shown for illustration porpuses. It does not exist in the \<volumetricstack> context.
The value sampled from the \<volumetricstack> element might be the result of blending multiple \<volumetriclayer>s in this stack, see Figure 4-1.

Figure 5-2c) Shows the \<volumetricstack> again. The unit box of the UVW coordinate system is shown as a wireframe. The transformation `T2` between \<volumetricstack> coordinate system and UVW space is given according to the `transform`-attribute of the \<channelfromimage3d> element in each \<volumetriclayer> of this \<volumetricstack>.

Figure 5-3d) Shows the UVW coordinate space and where the sampling point (+) is evaluated, and the UVW-locations to which the voxel centers of the \<image3d>-element map.

Figure 5-3e) illustrates where the sampling point (+) ends up in the voxel index space. The mapping of UVW to voxel indices in the \<image3d>-element is described in [Chapter 2. 3D Image](#chapter-2-3d-image).

_Figure 5-2: Illustration of the different coordinate systems and 3MF elements in the sampling process. a) the object to be sampled at position (+). b) A view into the \<volumetricstack>. The original clipping surface from a) is only shown for illustration porpuses. c) Shows the \<volumetricstack> again. The unit box of the UVW coordinate system is shown as a wireframe. d) The UVW coordinate space and the UVW-locations to which the voxel-centers map. e) The sampling point (+) in the voxel index space._
![Illustration of different coordinate systems in the sampling process](images/fig_coordinatesystems.png)



# Part II. Appendices

# Appendix A. Glossary

See [the standard 3MF Glossary](https://github.com/3MFConsortium/spec_resources/blob/master/glossary.md).

## Appendix B. 3MF XSD Schema for the Volumetric Extension
```xml
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns="http://schemas.microsoft.com/3dmanufacturing/volumetric/2018/11" xmlns:xs="http://www.w3.org/2001/XMLSchema"
xmlns:xml="http://www.w3.org/XML/1998/namespace" targetNamespace="http://schemas.microsoft.com/3dmanufacturing/volumetric/2018/11"
	elementFormDefault="unqualified" attributeFormDefault="unqualified" blockDefault="#all">
	<xs:annotation>
		<xs:documentation>
			<![CDATA[
		Schema notes:

		Items within this schema follow a simple naming convention of appending a prefix indicating the type of element for references:

		Unprefixed: Element names
		CT_: Complex types
		ST_: Simple types
		
		]]>
		</xs:documentation>
	</xs:annotation>
	<!-- Complex Types -->

	<xs:complexType name="CT_Resources">
		<xs:sequence>
			<xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="2147483647"/>
			<xs:element ref="image3d" minOccurs="0" maxOccurs="2147483647"/>
			<xs:element ref="channelfromimage3d" minOccurs="0" maxOccurs="2147483647"/>
			<xs:element ref="volumetricstack" minOccurs="0" maxOccurs="2147483647"/>
		</xs:sequence>
		<xs:anyAttribute namespace="##other" processContents="lax"/>
	</xs:complexType>

	<xs:complexType name="CT_Image3D">
		<xs:sequence>
			<xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="2147483647"/>
			<xs:element ref="image3dsheet" minOccurs="0" maxOccurs="2147483647"/>
		</xs:sequence>
		<xs:attribute name="id" type="ST_ResourceID" use="required"/>
		<xs:attribute name="name" type="xs:string" use="required"/>
		<xs:attribute name="rowcount" type="xs:positiveInteger" use="required"/>
		<xs:attribute name="columncount" type="xs:positiveInteger" use="required"/>
		<xs:attribute name="sheetcount" type="xs:positiveInteger" use="required"/>
		<xs:anyAttribute namespace="##other" processContents="lax"/>
	</xs:complexType>

	<xs:complexType name="CT_Image3DSheet">
		<xs:sequence>
			<xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="2147483647"/>
		</xs:sequence>
		<xs:attribute name="path" type="ST_UriReference" use="required"/>
    <xs:attribute name="valueoffset" type="ST_Number" use="optional" default="0.0"/>
    <xs:attribute name="valuescale" type="ST_Number" use="optional" default="1.0"/>
		<xs:anyAttribute namespace="##other" processContents="lax"/>
	</xs:complexType>

	<xs:complexType name="CT_VolumetricStack">
		<xs:sequence>
			<xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="2147483647"/>
			<xs:element ref="dstchannel" minOccurs="1" maxOccurs="65535"/>
			<xs:element ref="volumetriclayer" minOccurs="1" maxOccurs="65535"/>
		</xs:sequence>
		<xs:attribute name="id" type="ST_ResourceID" use="required"/>
		<xs:anyAttribute namespace="##other" processContents="lax"/>
	</xs:complexType>

	<xs:complexType name="CT_Channel">
		<xs:sequence>
			<xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="2147483647"/>
		</xs:sequence>
		<xs:attribute name="name" type="ST_ChannelName" use="required"/>
		<xs:attribute name="background" type="ST_Number" use="optional" default="0"/>
		<xs:anyAttribute namespace="##other" processContents="lax"/>
	</xs:complexType>
	
	<xs:complexType name="CT_VolumetricLayer">
		<xs:sequence>
			<xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="2147483647"/>
			<xs:element ref="channelmapping" minOccurs="1" maxOccurs="2147483647"/>
		</xs:sequence>
		<xs:attribute name="blendmethod" type="ST_BlendMethod" use="required"/>
		<xs:attribute name="srcalpha" type="ST_Number" use="optional"/>
		<xs:attribute name="dstalpha" type="ST_Number" use="optional"/>
		<xs:attribute name="maskid" type="ST_ResourceId" use="optional"/>
		<xs:anyAttribute namespace="##other" processContents="lax"/>
	</xs:complexType>

	<xs:complexType name="CT_ChannelFromImage3D">
		<xs:sequence>
			<xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="2147483647"/>
		</xs:sequence>
		<xs:attribute name="id" type="ST_ResourceID" use="required"/>
		<xs:attribute name="image3did" type="ST_ResourceID" use="required"/>
		<xs:attribute name="channel" type="ST_ChannelName" use="required"/>
		<xs:attribute name="transform" type="ST_Matrix3D" use="required"/>
		<xs:attribute name="filter" type="ST_Filter" use="optional" default="linear"/>
		<xs:attribute name="valueoffset" type="ST_Number" use="optional" default="0.0"/>
		<xs:attribute name="valuescale" type="ST_Number" use="optional" default="1.0"/>
		<xs:attribute name="tilestyleu" type="ST_TileStyle" use="optional" default="wrap"/>
		<xs:attribute name="tilestylev" type="ST_TileStyle" use="optional" default="wrap"/>
		<xs:attribute name="tilestylew" type="ST_TileStyle" use="optional" default="wrap"/>
		<xs:anyAttribute namespace="##other" processContents="lax"/>
	</xs:complexType>

	<xs:complexType name="CT_ChannelMapping">
		<xs:sequence>
			<xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="2147483647"/>
		</xs:sequence>
		<xs:attribute name="sourceid" type="ST_ResourceID" use="required"/>
		<xs:attribute name="dstchannel" type="ST_ChannelName" use="required"/>
		<xs:anyAttribute namespace="##other" processContents="lax"/>
	</xs:complexType>

	<xs:complexType name="CT_Mesh">
		<xs:sequence>
			<xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="2147483647"/>
			<xs:element ref="volumedata" minOccurs="0" maxOccurs="1"/>
		</xs:sequence>
	</xs:complexType>

	<xs:complexType name="CT_VolumeData">
		<xs:sequence>
				<xs:element ref="boundary" minOccurs="0" maxOccurs="1"/>
				<xs:element ref="composite" minOccurs="0" maxOccurs="1"/>
				<xs:element ref="color" minOccurs="0" maxOccurs="1"/>
				<xs:element ref="property" minOccurs="0" maxOccurs="2147483647"/>
				<xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="2147483647"/> 
		</xs:sequence>
		<xs:anyAttribute namespace="##other" processContents="lax"/>
	</xs:complexType>

	<xs:complexType name="CT_Boundary">
		<xs:sequence>
			<xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="2147483647"/>
		</xs:sequence>
		<xs:attribute name="sourceid" type="ST_ResourceID" use="required" />
		<xs:attribute name="transform" type="ST_Matrix3D" use="required" />
		<xs:attribute name="channel" type="ST_ChannelName" use="required" />
		<xs:attribute name="solidthreshold" type="ST_Number" use="optional" default="0" />
		<xs:anyAttribute namespace="##other" processContents="lax"/>
	</xs:complexType>

	<xs:complexType name="CT_Color">
		<xs:sequence>
			<xs:element ref="red"/>
			<xs:element ref="green"/>
			<xs:element ref="blue"/>
			<xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="2147483647"/>
		</xs:sequence>
		<xs:attribute name="sourceid" type="ST_ResourceID" use="required" />
		<xs:attribute name="transform" type="ST_Matrix3D" use="required" />
		<xs:anyAttribute namespace="##other" processContents="lax"/>
	</xs:complexType>

	<xs:complexType name="CT_ColorChannel">
		<xs:sequence>
			<xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="2147483647"/>
		</xs:sequence>
		<xs:attribute name="channel" type="ST_ChannelName" use="required" />
		<xs:anyAttribute namespace="##other" processContents="lax"/>
	</xs:complexType>

	<xs:complexType name="CT_Composite">
		<xs:sequence>
			<xs:element ref="materialmapping" minOccurs="1" maxOccurs="2147483647"/>
			<xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="2147483647"/>
		</xs:sequence>
		<xs:attribute name="sourceid" type="ST_ResourceID" use="required" />
		<xs:attribute name="transform" type="ST_Matrix3D" use="required" />
		<xs:attribute name="basematerialid" type="ST_ResourceID" use="required" />
		<xs:anyAttribute namespace="##other" processContents="lax"/>
	</xs:complexType>

		<xs:complexType name="CT_MaterialMapping">
		<xs:sequence>
			<xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="2147483647"/>
		</xs:sequence>
		<xs:attribute name="channel" type="ST_ChannelName" use="required" />
		<xs:attribute name="pindex" type="ST_ResourceIndex" use="required" />
		<xs:anyAttribute namespace="##other" processContents="lax"/>
	</xs:complexType>

	<xs:complexType name="CT_Property">
		<xs:sequence>
			<xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="2147483647"/>
		</xs:sequence>
		<xs:attribute name="sourceid" type="ST_ResourceID" use="required" />
		<xs:attribute name="transform" type="ST_Matrix3D" use="required" />
		<xs:attribute name="channel" type="ST_ChannelName" use="required" />
		<xs:attribute name="name" type="xs:QName" use="required" />
		<xs:attribute name="required" type="xs:boolean" use="required" />
		<xs:anyAttribute namespace="##other" processContents="lax"/>
	</xs:complexType>

	<!-- Simple Types -->
	<xs:simpleType name="ST_TileStyle">
		<xs:restriction base="xs:string">
			<xs:enumeration value="wrap"/>
			<xs:enumeration value="mirror"/>
			<xs:enumeration value="clamp"/>
			<xs:enumeration value="none"/>
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="ST_Filter">
		<xs:restriction base="xs:string">
			<xs:enumeration value="nearest"/>
			<xs:enumeration value="linear"/>
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="ST_ResourceID">
		<xs:restriction base="xs:positiveInteger">
			<xs:maxExclusive value="2147483648"/>
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="ST_ResourceIndex">
		<xs:restriction base="xs:nonNegativeInteger">
			<xs:maxExclusive value="2147483648"/>
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="ST_UriReference">
		<xs:restriction base="xs:anyURI">
			<xs:pattern value="/.*"/>
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="ST_ChannelName">
		<xs:restriction base="xs:string">
			<xs:enumeration value="R"/>
			<xs:enumeration value="G"/>
			<xs:enumeration value="B"/>
			<xs:enumeration value="A"/>
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="ST_Number">
		<xs:restriction base="xs:double">
			<xs:whiteSpace value="collapse"/>
			<xs:pattern value="((\-|\+)?(([0-9]+(\.[0-9]+)?)|(\.[0-9]+))((e|E)(\-|\+)?[0-9]+)?)"/>
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="ST_BlendMethod">
		<xs:restriction base="xs:string">
			<xs:enumeration value="mix"/>
			<xs:enumeration value="multiply"/>
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="ST_Matrix3D">
		<xs:restriction base="xs:string">
			<xs:whiteSpace value="collapse"/>
			<xs:pattern value="((\-|\+)?(([0-9]+(\.[0-9]+)?)|(\.[0-9]+))((e|E)(\-|\+)?[0-9]+)?) ((\-|\+)?(([0-9]+(\.[0-9]+)?)|(\.[0-9]+))((e|E)(\-|\+)?[0-9]+)?) ((\-|\+)?(([0-9]+(\.[0-9]+)?)|(\.[0-9]+))((e|E)(\-|\+)?[0-9]+)?) ((\-|\+)?(([0-9]+(\.[0-9]+)?)|(\.[0-9]+))((e|E)(\-|\+)?[0-9]+)?) ((\-|\+)?(([0-9]+(\.[0-9]+)?)|(\.[0-9]+))((e|E)(\-|\+)?[0-9]+)?) ((\-|\+)?(([0-9]+(\.[0-9]+)?)|(\.[0-9]+))((e|E)(\-|\+)?[0-9]+)?) ((\-|\+)?(([0-9]+(\.[0-9]+)?)|(\.[0-9]+))((e|E)(\-|\+)?[0-9]+)?) ((\-|\+)?(([0-9]+(\.[0-9]+)?)|(\.[0-9]+))((e|E)(\-|\+)?[0-9]+)?) ((\-|\+)?(([0-9]+(\.[0-9]+)?)|(\.[0-9]+))((e|E)(\-|\+)?[0-9]+)?) ((\-|\+)?(([0-9]+(\.[0-9]+)?)|(\.[0-9]+))((e|E)(\-|\+)?[0-9]+)?) ((\-|\+)?(([0-9]+(\.[0-9]+)?)|(\.[0-9]+))((e|E)(\-|\+)?[0-9]+)?) ((\-|\+)?(([0-9]+(\.[0-9]+)?)|(\.[0-9]+))((e|E)(\-|\+)?[0-9]+)?)"/>
		</xs:restriction>
	</xs:simpleType>

	<!-- Elements -->
	<xs:element name="image3d" type="CT_Image3D"/>
	<xs:element name="image3dsheet" type="CT_Image3DSheet"/>
	<xs:element name="volumetricstack" type="CT_VolumetricStack"/>
	<xs:element name="channel" type="CT_Channel"/>
	<xs:element name="dstchannel" type="CT_Channel"/>
	<xs:element name="volumetriclayer" type="CT_VolumetricLayer"/>
  <xs:element name="channelmapping" type="CT_ChannelMapping"/>
	<xs:element name="channelfromimage3d" type="CT_ChannelFromImage3D"/>
	<xs:element name="volumedata" type="CT_VolumeData"/>
	<xs:element name="boundary" type="CT_Boundary"/>
	<xs:element name="composite" type="CT_Composite"/>
	<xs:element name="materialmapping" type="CT_MaterialMapping"/>
	<xs:element name="color" type="CT_Color"/>
	<xs:element name="red" type="CT_ColorChannel"/>
	<xs:element name="green" type="CT_ColorChannel"/>
	<xs:element name="blue" type="CT_ColorChannel"/>
	<xs:element name="property" type="CT_Property"/>
	<xs:element name="mesh" type="CT_Mesh"/>
</xs:schema>
```

# Appendix C. Standard Namespace

Volumetric [http://schemas.microsoft.com/3dmanufacturing/volumetric/2018/11](http://schemas.microsoft.com/3dmanufacturing/volumetric/2018/11)

# Appendix D: Example file

3dmodel.model-file corresponding to the structure in Figure-3-3 b:
```xml
<?xml version="1.0" encoding="utf-8"?>
<model xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" unit="millimeter" xml:lang="en-US" 
xmlns:v="http://schemas.microsoft.com/3dmanufacturing/volumetric/2018/11" >
	<resources>
		<v:image3d id="1" rowcount="3" columncount="4" sheetcount="2">
			<image3dsheet path="/3D/volumetric/colors/sheet 0.png" valuescale="0.00392156862"/>
			<image3dsheet path="/3D/volumetric/colors/sheet 1.png" valuescale="0.00392156862"/>
		</v:image3d>
		<v:channelfromimage3d id="2" image3did="1" channelname="R" tilestyleu="wrap" tilestylev="wrap" tilestylew="wrap"/>
		<v:channelfromimage3d id="3" image3did="1" channelname="G" tilestyleu="wrap" tilestylev="wrap" tilestylew="wrap"/>
		<v:channelfromimage3d id="4" image3did="1" channelname="B" tilestyleu="wrap" tilestylev="wrap" tilestylew="wrap"/>
		<v:volumetricstack id="5" >
			<dstchannel name="red" background="0"/>
			<dstchannel name="green" background="0"/>
			<dstchannel name="blue" background="0"/>
			
			<volumetriclayer blendmethod="max">
				<channelmapping sourceid="2" dstchannel="red"/>
				<channelmapping sourceid="3" dstchannel="green"/>
				<channelmapping sourceid="4" dstchannel="blue"/>
			</volumetriclayer>
		</v:volumetricstack>
		
		<object id="6" name="Body1" type="model">
			<mesh>
				<vertices>
					<vertex x="200" y="100" z="75" />
					<vertex x="-100" y="100" z="75" />
					<vertex x="-100" y="16.66667" z="75" />
					<vertex x="200" y="16.66667" z="75" />
					<vertex x="-100" y="100" z="-100" />
					<vertex x="200" y="100" z="-100" />
					<vertex x="200" y="16.66667" z="-100" />
					<vertex x="-100" y="16.66667" z="-100" />
				</vertices>
				<triangles>
					<triangle v1="1" v2="2" v3="0" />
					<triangle v1="0" v2="2" v3="3" />
					<triangle v1="5" v2="6" v3="4" />
					<triangle v1="4" v2="6" v3="7" />
					<triangle v1="3" v2="6" v3="0" />
					<triangle v1="0" v2="6" v3="5" />
					<triangle v1="2" v2="7" v3="3" />
					<triangle v1="3" v2="7" v3="6" />
					<triangle v1="1" v2="4" v3="2" />
					<triangle v1="2" v2="4" v3="7" />
					<triangle v1="0" v2="5" v3="1" />
					<triangle v1="1" v2="5" v3="4" />
				</triangles>
				<v:volumedata>
					<color sourceid="3" transform="0.01 0 0 0 0.0133333333333 0 0 0 0.02 0 0 0">
						<red channel="red"/>
						<green channel="green"/>
						<blue channel="blue"/>
					</color>
				</v:volumedata>
			</mesh>
		</object>
	</resources>
	<build>
		<item objectid="6"/>
	</build>
</model>

```

_sheet0.png_
![sheet0.png](images/sheet0.png)

_sheet1.png_
![sheet1.png](images/sheet1.png)

# References

[1] Pasko, Alexander, et al. "Function representation in geometric modeling: concepts, implementation and applications." The visual computer 11.8 (1995): 429-446.

[2] Wyvill, Brian, Andrew Guy, and Eric Galin. "Extending the csg tree. warping, blending and boolean operations in an implicit surface modeling system." Computer Graphics Forum. Vol. 18. No. 2. Oxford, UK and Boston, USA: Blackwell Publishers Ltd, 1999.

See also [the standard 3MF References](https://github.com/3MFConsortium/spec_resources/blob/master/references.md).

Copyright 3MF Consortium 2021.
